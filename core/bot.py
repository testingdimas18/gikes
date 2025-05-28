# gikes/bot/core/bot.py
from pyrogram import Client
from bot.config import BOT_TOKEN, API_ID, API_HASH

bot_instance = Client("gikes_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)