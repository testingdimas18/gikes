# gikes/bot/core/handlers/admin.py
from pyrogram import Client, filters
from bot.core.bot import bot_instance
from bot.core.database.mongodb import db  # Import instance database global
from bot.config import OWNER_ID

@bot_instance.on_message(filters.command(["ankes_on", "ankes"]) & filters.user(OWNER_ID))
async def ankes_on(client, message):
    chat_id = message.chat.id
    db.set_bot_status(chat_id, True)
    await message.reply_text("Bot diaktifkan (oleh pemilik).")

@bot_instance.on_message(filters.command("ankes_off") & filters.user(OWNER_ID))
async def ankes_off(client, message):
    chat_id = message.chat.id
    db.set_bot_status(chat_id, False)
    await message.reply_text("Bot dinonaktifkan (oleh pemilik).")

@bot_instance.on_message(filters.command("addfree") & filters.user(OWNER_ID))
async def addfree(client, message):
    chat_id = message.chat.id
    if db.get_bot_status(chat_id):
        if len(message.command) > 1 and message.command[1].isdigit():
            user_id = int(message.command[1])
            db.add_free_user(user_id)
            await message.reply_text(f"User ID {user_id} ditambahkan ke daftar orang tanpa dosa (oleh pemilik).")
        else:
            await message.reply_text("Penggunaan: /addfree [User ID] (oleh pemilik)")
    else:
        await message.reply_text("Bot sedang tidak aktif.")

@bot_instance.on_message(filters.command("delfree") & filters.user(OWNER_ID))
async def delfree(client, message):
    chat_id = message.chat.id
    if db.get_bot_status(chat_id):
        if len(message.command) > 1 and message.command[1].isdigit():
            user_id = int(message.command[1])
            deleted_count = db.delete_free_user(user_id)
            if deleted_count > 0:
                await message.reply_text(f"User ID {user_id} dihapus dari daftar orang tanpa dosa (oleh pemilik).")
            else:
                await message.reply_text(f"User ID {user_id} tidak ditemukan di daftar orang tanpa dosa.")
        else:
            await message.reply_text("Penggunaan: /delfree [User ID] (oleh pemilik)")
    else:
        await message.reply_text("Bot sedang tidak aktif.")

@bot_instance.on_message(filters.command("promote") & filters.user(OWNER_ID))
async def promote(client, message):
    if len(message.command) == 3:
        try:
            user_id_to_promote = int(message.command[1])
            role_to_assign = message.command[2].lower()
            if db.promote_user(user_id_to_promote, role_to_assign):
                await message.reply_text(f"Pengguna dengan ID {user_id_to_promote} berhasil dipromosikan menjadi {role_to_assign} (oleh pemilik).")
            else:
                await message.reply_text(f"Peran '{role_to_assign}' tidak valid.")
        except ValueError:
            await message.reply_text("Penggunaan: /promote [User ID] [owner|sudo|free|admin] (oleh pemilik)")
    else:
        await message.reply_text("Penggunaan: /promote [User ID] [owner|sudo|free|admin] (oleh pemilik)")