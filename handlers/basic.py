# gikes/bot/core/handlers/basic.py
from pyrogram import Client, filters
from bot.core.bot import bot_instance
from bot.core.keyboards import main as main_keyboard
from bot.core.keyboards import help as help_keyboard
from pyrogram.types import ReplyKeyboardRemove
from bot.config import OWNER_ID  # Import OWNER_ID

BOT_USERNAME = "@AnkesClayBot"  # Ganti dengan username bot Anda

@bot_instance.on_message(filters.command("start"))
async def start(client, message):
    start_text = (
        f"Woy Kontol {message.from_user.first_name or ''}!\n"
        f"Di Pake: 0 group\n"
        f"Halo Gua {BOT_USERNAME}\n"
        f"Gua adalah Bot Anti Gcast Buat Ngehapusin Gikesan Ampas Yang Ada Di Gc Lu Ya Anjing."
    )
    await message.reply_text(start_text, reply_markup=main_keyboard.keyboard, quote=True)

@bot_instance.on_callback_query(filters.regex("^help_menu$"))
async def show_help_menu(client, callback_query):
    await callback_query.answer()
    await callback_query.edit_message_text("Berikut adalah menu bantuan:", reply_markup=help_keyboard.keyboard)

@bot_instance.on_callback_query(filters.regex("^close_menu$"))
async def close_menu(client, callback_query):
    await callback_query.answer()
    await callback_query.edit_message_text("Menutup menu.", reply_markup=ReplyKeyboardRemove())

# Tidak ada handler callback query untuk invite_group lagi karena sudah berupa URL di keyboard

@bot_instance.on_message(filters.text & filters.regex("^Close$"))
async def handle_close_button(client, message):
    await message.reply_text("Menutup keyboard...", reply_markup=ReplyKeyboardRemove())
