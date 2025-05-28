# gikes/bot/config.py
import os

# Telegram Bot Token
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# MongoDB Connection URI
MONGO_URI = os.environ.get("MONGO_URI")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

# API ID dan API Hash dari Telegram (untuk Pyrogram)
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")

# User ID Pemilik Bot (untuk kontrol akses)
OWNER_ID = int(os.environ.get("OWNER_ID"))