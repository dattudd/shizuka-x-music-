import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "20798317"))
API_HASH = getenv("API_HASH", "82a94d416e05ca5cc3bc04da8494d7ca")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7062907555:AAEXu6nEUaj3G3EcN_lOJqoF6djz30HN8uE")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", "chinna")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "Lilly")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "lilly MUSIC")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "chiinnoda_assistant")
EVALOP = list(map(int, getenv("EVALOP", "6886160138").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://sanasomani786:TJgADfpkI1XVUkKt@cluster0.ruhyad9.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10000"))

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "18000")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002055640243"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6439286014"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/dattudd/Dfsxmusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/OVER_POWERED")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/OVER_POWERED")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400000")
)  # Remember to give value in Seconds


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "250"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 = getenv("STRING_SESSION", "BQCLowo82B8iskwWefr_9qAnuGm7qd9eK7w4YS1SrZnL1lidTNlQuEOD1hjpkogo_iig-tq4Qz7MsCZTacwQ8u0VxnimyflU71cG0qqT6PqxYHKMz5z-dcjO_ubRm0DfJ86yS16FPqTcvcx_1Oaw5vsQTF1H69U8zVlcpYkc2nkGsCR4L1SQZ1VbiMjMMtMS1y0EgzV-LpSMvmq2aQPU3-HVdiyGN4beksam-U9SqSQbWe9ujj5_Wy8n1HvHi6uUTKru_Nr0CdfysiQTPLjqVgoYosDOKUHk8trhbQNxupFDlLt9ei0qSVOlnKbiSfFnlGcZXvqhBTFZLWD-_ujq6JtUAAAAAZsJR20A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/e0191fb6701ef32bb8654.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/dec61e858d57c14343455.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/7795e58425337d0455e95.jpg"
STATS_IMG_URL = "https://telegra.ph/file/69d56bc410683716bafee.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
