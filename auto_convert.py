from bot.features.timetable.convert import convert_timetable
from main import loop


async def main() -> None:
    convert = loop.create_task(convert_timetable(True))
    await convert


if __name__ == "__main__":
    loop.run_until_complete(main())
