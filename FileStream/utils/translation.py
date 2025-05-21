from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>Hai, saya adalah PikaStreambot.</b>\n\n
<i>Saya bisa membuat stream link dari file Telegram dan bisa dishare ataupun stream di berbagai platform.</i>
"""

    HELP_TEXT = """
<b>- Jika di private, cukup kirimkan file atau video dan dapatkan link stream dari file/video anda</b>\n
<b>- Jika di group, cukup reply file/video dengan perintah /stream dan dapatkan link stream dari file/video anda</b>\n"""

    ABOUT_TEXT = """
<b>Nama bot : {}</b>\n
<b>Versi : {}</b>
<b>Update : 19-Mei-2025</b>
<b>Maintainer : <a href='https://telegram.me/pikadotchu'>𝑷𝒊𝒌𝒂𝒄𝒉𝒖</a></b>\n
"""

    STREAM_TEXT = """
<b>📂 Nama File :</b> <code>{}</code>\n
<b>📦 Ukuran :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<b>📂 Nama File :</b> <code>{}</code>\n
<b>📦 Ukuran :</b> <code>{}</code>\n"""


    BAN_TEXT = "**Anda tidak diizinkan menggunakan bot ini**"


class BUTTON(object):
    def START_BUTTONS(uid):
        InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Bantuan', callback_data='help'),
            InlineKeyboardButton('Tentang', callback_data='about'),
            InlineKeyboardButton('Tutup', callback_data='close')
        ],
            [InlineKeyboardButton("📢 Channel Update", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    def HELP_BUTTONS(uid):
        InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Bantuan', callback_data='help'),
            InlineKeyboardButton('Tentang', callback_data='about'),
            InlineKeyboardButton('Tutup', callback_data='close')
        ],
            [InlineKeyboardButton("📢 Channel Update", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    def ABOUT_BUTTONS(uid):
        InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Bantuan', callback_data='help'),
            InlineKeyboardButton('Tentang', callback_data='about'),
            InlineKeyboardButton('Tutup', callback_data='close')
        ],
            [InlineKeyboardButton("📢 Channel Update", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
