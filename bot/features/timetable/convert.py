import shutil
import subprocess
from pathlib import Path
from loguru import logger

from pdf2image import convert_from_path

from bot.features.timetable import notifications as notif
# Need install "poppler" and libreoffice


async def convert_doc(bad_doc, locate):
    try:
        subprocess.call(  # use libreoffice to convert, quality 60/100...
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
        bad_doc.unlink()  # dellete used doc
        return True
    except Exception as e:
        logger.error(f"Converting docx error: {e}")
        await notif.cmd_notify_admins(
            f"""
        Ошибка при конвертации расписания в pdf!

        {e}
        """
        )
        return False


async def convert_pdf(bad_pdf, locate):
    try:
        images = convert_from_path(f"{bad_pdf}", 100)  # use pdf2image to convert
        for i, image in enumerate(images):  # save result for all pages
            image.save(f"{locate}/{i}.png", "PNG")
            return True
    except Exception as e:
        shutil.move(swap, png)
        logger.error(f"Coverting pdf error: {e}")
        await notif.cmd_notify_admins(
            f"""
        Ошибка при конвертации расписания в png!

        {bad_pdf}

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


async def convert_timetable(auto=False):
    await paths()
    for file in new_doc:
        shutil.copy(str(file), str(doc))
        file.unlink()
    if doc.is_file():
        shutil.rmtree(swap)
        shutil.move(png, swap)
        png.mkdir()
        if await convert_doc(doc, module):
            await notif.save_pdf(pdf)
        if await convert_pdf(pdf, png):
            await notif.cmd_notify_admins("Расписание успешно сконвертировано!")
            if not auto:
                logger.info("Timetable converted manual")
            else:
                logger.info("Timetable converted automatically")
    else:
        if not auto:
            await notif.cmd_notify_admins(
                "Конвертация не удалась, так как нечего конвертировать :)"
            )
            logger.info("Manual coverting failed")


# async def auto_convert_timetable():
#     if doc.is_file():
#         await convert_doc(doc, pdf)
#         await notif.save_pdf(pdf)
#         await convert_pdf(pdf, png)
#         logger.info("Timetable converted!")


# if doc.is_file():
#     # print("rm SWAP")
#     # shutil.rmtree(SWAP)
#     # print("swaping today and mkdir")
#     # PNG.replace(SWAP)
#     # PNG.mkdir()
#     print("converting DOCX-PDF")
#     convert_doc(doc)
#     print("converting PDF-PNG")
#     convert_pdf(pdf, png)
#     print("Successful!")
# else:
#     print("nothing to convert")

