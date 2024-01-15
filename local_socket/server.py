import asyncio
import json
from loguru import logger
from main import loop
from local_socket.data_handler import process_data

# TODO
# [x] Защита от DoS-атак
# [x] Обработка исключений в основном цикле
# [x] Логирование
# [x] Аутентификация
# [] Проверка входных данных

ALLOWED_IPS = {"127.0.0.1"}  # Замените на список разрешенных IP-адресов
MAX_CONNECTIONS = 10  # Максимальное количество одновременных соединений


class ServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.client_ip = transport.get_extra_info("peername")[0]

        if self.client_ip not in ALLOWED_IPS:
            print(f"Connection from {self.client_ip} not allowed.")
            transport.close()
            return

        # Проверка на максимальное количество соединений
        current_connections = len(asyncio.all_tasks())
        if current_connections > MAX_CONNECTIONS:
            logger.warning(f"Too many connections. Rejecting {self.client_ip}")
            transport.close()
            return

        self.transport = transport
        self.buffer = b""

    # Cохранение данных, которые приходят асинхронно
    # Данные могут приходить фрагментированно
    # Накапливаем этих фрагменты до тех пор,
    # пока не будет полностью получено целое сообщение
    def data_received(self, data):
        self.buffer += data
        loop.create_task(self.process_data())

    # Извлекаем из буфера полные сообщения,
    # завершенные символом новой строки
    async def process_data(self):
        while b"}" in self.buffer:
            closing_bracket_index = self.buffer.find(b"}")
            # Извлечение данных от начала строки до закрывающей скобки
            message = self.buffer[: closing_bracket_index + 1]
            # Обновление буфера, оставив остаток строки после закрывающей скобки
            self.buffer = self.buffer[closing_bracket_index + 1 :]

            # Проверяем, является ли извлеченная строка корректным JSON
            try:
                json_message = json.loads(message.decode("utf-8"))
            except json.JSONDecodeError:
                # Произошла ошибка при декодировании JSON, пропускаем сообщение
                continue

            response = await process_data(self.client_ip, json_message)
            self.transport.write(response)

    def connection_lost(self, exc):
        pass
        # logger.info(f"Connection from {self.client_ip} closed.")


async def start_server():
    server = await loop.create_server(ServerProtocol, "127.0.0.1", 8888)

    addr = server.sockets[0].getsockname()
    logger.info(f"Socket is running at {addr}")

    async with server:
        await server.serve_forever()


loop.create_task(start_server())
