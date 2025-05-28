# gikes/bot/core/handlers/blacklist.py
from pyrogram import Client, filters
from bot.core.bot import bot_instance
from bot.core.database.mongodb import db  # Import instance database global

@bot_instance.on_message(filters.command("addbl"))
async def addbl(client, message):
    user_id = message.from_user.id
    if db.is_sudo(user_id):
        if len(message.command) > 1:
            word = " ".join(message.command[1:])
            db.add_blacklisted_word(word)
            await message.reply_text(f"Kata '{word}' ditambahkan ke blacklist (oleh sudo/owner).")
        else:
            await message.reply_text("Penggunaan: /addbl [kata] (oleh sudo/owner)")
    else:
        await message.reply_text("Anda tidak memiliki izin untuk menjalankan perintah ini.")

@bot_instance.on_message(filters.command("delbl"))
async def delbl(client, message):
    user_id = message.from_user.id
    if db.is_sudo(user_id):
        if len(message.command) > 1:
            word = " ".join(message.command[1:])
            deleted_count = db.delete_blacklisted_word(word)
            if deleted_count > 0:
                await message.reply_text(f"Kata '{word}' dihapus dari blacklist (oleh sudo/owner).")
            else:
                await message.reply_text(f"Kata '{word}' tidak ditemukan di blacklist.")
        else:
            await message.reply_text("Penggunaan: /delbl [kata] (oleh sudo/owner)")
    else:
        await message.reply_text("Anda tidak memiliki izin untuk menjalankan perintah ini.")

@bot_instance.on_message(filters.command("listbl"))
async def listbl(client, message):
    user_id = message.from_user.id
    if db.is_sudo(user_id):
        blacklisted_words = db.get_blacklisted_words()
        if blacklisted_words:
            response = "Daftar kata yang diblacklist:\n" + "\n".join(blacklisted_words)
        else:
            response = "Tidak ada kata yang diblacklist saat ini."
        await message.reply_text(response)
    else:
        await message.reply_text("Anda tidak memiliki izin untuk menjalankan perintah ini.")

@bot_instance.on_message(filters.command("addblack") & filters.reply)
async def addblack_reply(client, message):
    user_id = message.from_user.id
    if db.is_sudo(user_id):
        replied_user_id = message.reply_to_message.from_user.id
        db.add_blacklisted_user(replied_user_id)
        await message.reply_text(f"User ID {replied_user_id} diblacklist (oleh sudo/owner).")
    else:
        await message.reply_text("Anda tidak memiliki izin untuk menjalankan perintah ini.")

@bot_instance.on_message(filters.command("delblack"))
async def delblack_user(client, message):
    user_id = message.from_user.id
    if db.is_sudo(user_id):
        if len(message.command) > 1 and message.command[1].isdigit():
            user_id_to_unblacklist = int(message.command[1])
            deleted_count = db.delete_blacklisted_user(user_id_to_unblacklist)
            if deleted_count > 0:
                await message.reply_text(f"User ID {user_id_to_unblacklist} dihapus dari blacklist (oleh sudo/owner).")
            else:
                await message.reply_text(f"User ID {user_id_to_unblacklist} tidak ditemukan di blacklist.")
        else:
            await message.reply_text("Penggunaan: /delblack [User ID] (oleh sudo/owner