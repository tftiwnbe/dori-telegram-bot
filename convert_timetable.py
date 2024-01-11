import asyncio
import json
from bot.features.timetable.auto_convert import convert_timetable


async def send_notification(data):
    try:
        reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

        encoded_data = json.dumps(data).encode()
        writer.write(encoded_data)
        await writer.drain()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        writer.close()
        await writer.wait_closed()


async def main() -> None:
    convert = await convert_timetable()
    if convert == 0:
        return
    elif convert == 1:
        data = {
            "notify_admin": "Расписание успешно сконвертировано!",
            "timetable": True,
        }
    else:
        data = {"notify_admin": convert}
    await send_notification(data)


if __name__ == "__main__":
    asyncio.run(main())
