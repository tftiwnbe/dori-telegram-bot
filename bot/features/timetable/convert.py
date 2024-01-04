import shutil
import subprocess
from pathlib import Path
from loguru import logger

from pdf2image import convert_from_path

from bot.features.timetable.notifications import notify_timetable_subs
from bot.admin.notifications import notify_admin

# Need install "poppler" and libreoffice


async def convert_doc(bad_doc, locate):
    try:
        subprocess.call(  # use libreoffice to convert
            [
                "libreoffice",
                "lowriter",
                "--headless",
                "--convert-to",
                "pdf",
                "--outdir",
                locate,
                bad_doc,
            ]
        )
        bad_doc.unlink()  # delete used doc
        return True
    except Exception as e:
        logger.error(f"Converting docx error: {e}")
        await notify_admin(
            f"""
        Ошибка при конвертации расписания в pdf!

        {e}
        """
        )
        return False


async def convert_pdf(bad_pdf, locate):
    try:
        images = convert_from_path(f"{bad_pdf}", 310)  # use pdf2image to convert
        for i, image in enumerate(images):  # save result for all pages
            image.save(f"{locate}/{i}.png", "PNG")
            # logger.debug(f"Saving {locate}/{i}.png")
        return True
    except Exception as e:
        shutil.move(swap, png)
        logger.error(f"Coverting pdf error: {e}")
        await notify_admin(
            f"""
        Ошибка при конвертации расписания в png!

        {e}
        """
        )
        return False


async def paths():
    global module
    global new_doc
    global doc
    global pdf
    global swap
    global png

    module = Path("/home", "dori", "bot", "features", "timetable")
    new_doc = Path("/home", "nas_share", "01_Расписание", "00_Завтра").glob("*.docx")
    www_png = Path("/home", "nas_web")

    doc = Path(module, "Расписание.docx")
    pdf = Path(module, "Расписание.pdf")
    png = Path(www_png, "00_today/")
    swap = Path(module, "SWAP/")


async def convert_timetable():
    await paths()
    for file in new_doc:
        shutil.copy(str(file), str(doc))
        file.unlink()
    if doc.is_file():
        shutil.rmtree(swap)
        shutil.move(png, swap)
        png.mkdir()
        if await convert_doc(doc, module):
            await notify_timetable_subs()
            if await convert_pdf(pdf, png):
                await notify_admin("Расписание успешно сконвертировано!")
                logger.info("Timetable converted manual")
    else:
        await notify_admin("Конвертация не удалась, так как нечего конвертировать :)")
        logger.info("Manual coverting failed")
