#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1664850827
    OWNER = config("OWNER")
    ffmpegcode = ["-preset veryfast -c:v libx265 -s 940x540 -metadata 'title=@PX_07' -pix_fmt yuv420p -crf 33 -c:a libopus -b:a 30k -c:s copy -map 0"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
