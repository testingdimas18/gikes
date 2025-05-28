# gikes/bot/core/keyboards/main.py
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import OWNER_ID

BOT_USERNAME = "nama_bot_anda"  # Ganti dengan username bot Anda

def create_main_keyboard():
    owner_link = f"tg://user?id={OWNER_ID}"
    invite_link = f"https://t.me/{BOT_USERNAME}?startgroup=true"
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Masukan Gua Ke Group", url=invite_link)],
            [InlineKeyboardButton("Help", callback_data="help_menu")],
            [InlineKeyboardButton("Owner", url=owner_link)],
            [InlineKeyboardButton("Close", callback_data="close_menu")],
        ]
    )

keyboard = create_main_keyboard()