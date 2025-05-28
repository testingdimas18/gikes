# gikes/bot/core/keyboards/help.py
from pyrogram.types import ReplyKeyboardMarkup

keyboard = ReplyKeyboardMarkup(
    [
        [">/ankes on / off Mengaktifkan Atau Menonaktifkan Ankes."],
        [">/addfree Untuk Menambahkan User Ke Daftar Orang Tanpa Dosa."],
        [">/delfree Untuk Menghapus Untuk Menghapus Orang Yang Sudah Najis."],
        [">/addbl [kata]-[alasan] Untuk Menambahkan Kata Ke Database."],
        [">/delbl [kata] Untuk Menghapus Kata Dari Database."],
        [">/listbl Untuk Melihat List Kata Kata Yang Sudah Di Blacklist."],
        [">/addblack [reply] Untuk Menambahkan Orang Yang Banyak Dosa."],
        [">/delblack [userid] Untuk Menghapus Orang Yang Banyak Dosa."],
        [">/getbl Untuk Melihat Orang Yang Banyak Dosa."],
        [">/teg Untuk mention/tag member di gc lu."],
        [">/cancel Untuk membatalkan tag all."],
        ["Back", "Close"],
    ],
    resize_keyboard=True
)