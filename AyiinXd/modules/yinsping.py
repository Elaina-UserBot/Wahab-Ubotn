# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import time
from datetime import datetime
from secrets import choice


from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd import DEVS, LUMITED
from AyiinXd.events import register
from .ping import get_readable_time


absen = [
    "**𝙃𝙖𝙙𝙞𝙧 𝙙𝙤𝙣𝙜 𝘽𝙖𝙣𝙜** 😁",
    "**𝙃𝙖𝙙𝙞𝙧 𝙆𝙖𝙠𝙖 𝙂𝙖𝙣𝙩𝙚𝙣𝙜** 😉",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 ** 😎",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝙂𝙖𝙣𝙩𝙚𝙣𝙜** 🥵",
    "**𝙃𝙖𝙙𝙞𝙧 𝙉𝙜𝙖𝙗** 😎",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝘼𝙗𝙖𝙣𝙜** 🥺",
    "**𝙎𝙞 𝘾𝙖𝙠𝙚𝙥 𝙃𝙖𝙙𝙞𝙧 𝘽𝙖𝙣𝙜** 😎",
    "**Hadir kak maap telat** 🥺",
    "**Hadir Tuan** 🙏🏻",
    "**Hadir Majikan** 🙏🏻",
    "**Hadir Sayang** 😳",
    "**Hadir Bro** 👍",
    "**Maaf ka habis nemenin si dia** 🥺",
    "**Maaf ka habis diewe Lumi** 🥺",
    "**Hadir Lumi Sayang** 😘",
    "**Hadir Sayang Akuuuuhhh** ☺️",
    "**Hadir cintakuuu** 🥰",
]

lumicakep = [
    "**𝙄𝙮𝙖 𝙇𝙪𝙢𝙞 𝙂𝙖𝙣𝙩𝙚𝙣𝙜 𝘽𝙖𝙣𝙜𝙚𝙩** 😍",
    "**𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝙂𝙖𝙠 𝘼𝙙𝙖 𝙇𝙖𝙬𝙖𝙣** 😚",
    "**𝙆𝙖𝙢𝙪 𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝘼𝙠𝙪 𝙆𝙖𝙣 𝙇𝙪𝙢** 😍",
    "**𝙄𝙮𝙖𝙖 𝙜𝙖𝙙𝙖 𝙖𝙙𝙖 𝙨𝙖𝙞𝙣𝙜** 😎",
    "**𝙆𝙖𝙢𝙪 𝙅𝙖𝙢𝙚𝙩 𝙏𝙖𝙥𝙞 𝘽𝙤𝙤𝙣𝙜** 😚",
]

lumimarah = [
    "**𝙡𝙪𝙢𝙞 𝙨𝙖𝙮𝙖𝙣𝙜 𝙠𝙚𝙣𝙖𝙥𝙖𝙖?** 🥺",
    "**𝙅𝙖𝙣𝙜𝙖𝙣 𝙢𝙖𝙧𝙖𝙝 𝙢𝙖𝙧𝙖𝙝 𝙨𝙖𝙮𝙖𝙣𝙜𝙠𝙪𝙪, 𝙣𝙖𝙣𝙩𝙞 𝙖𝙠𝙪 𝙚𝙬𝙚 𝙣𝙞𝙝** 🥰",
    "**𝙅𝙖𝙣𝙜𝙖𝙣 𝙢𝙖𝙧𝙖𝙝 𝙢𝙖𝙧𝙖𝙝 𝙎𝙖𝙮𝙖𝙣𝙜, 𝙨𝙞𝙣𝙞 𝙖𝙠𝙪 𝙥𝙚𝙡𝙪𝙠** 🤗",
    "**𝙨𝙖𝙗𝙖𝙧 𝙮𝙖 𝙡𝙪𝙢𝙞 𝙨𝙖𝙮𝙖𝙣𝙜** 🫶",
    "**𝙜𝙖 𝙗𝙤𝙡𝙚𝙝 𝙣𝙜𝙤𝙢𝙤𝙣𝙜 𝙠𝙖𝙨𝙖𝙧 𝙨𝙖𝙮𝙖𝙣𝙜** 😡",
]

@register(incoming=True, from_users=DEVS, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**× ʟᴜᴍɪᴇʀᴇ ᴜsᴇʀʙᴏᴛ ×**\n\n× **ᴘɪɴɢᴇʀ :** `{} ms`\n× **ᴜᴘᴛɪᴍᴇ :** `{}`\n× **ᴏᴡɴᴇʀ :** `{}`\n× **ɪᴅ :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )


# KALO NGEFORK absen ini GA USAH DI HAPUS YA GOBLOK 😡
# JANGAN DI HAPUS GOBLOK 😡 LU COPY AJA TINGGAL TAMBAHIN
# DI HAPUS GUA GBAN YA 🥴 GUA TANDAIN LU AKUN TELENYA 😡

# Absen by : mrismanaziz <https://github.com/mrismanaziz/man-userbot>

@register(incoming=True, from_users=DEVS, pattern=r"^absen$")
async def lumiabsen(ganteng):
    await ganteng.reply(choice(absen))

@register(incoming=True, from_users=DEVS, pattern=r"^Sayang$")
async def lumi(lumi):
    await lumi.reply("**Iya hadir sayangku**😡❤️")

@register(incoming=True, from_users=DEVS, pattern=r"^Aku ganteng kan$")
async def lumi(ganteng):
    await ganteng.reply(choice(lumicakep))

@register(incoming=True, from_users=DEVS, pattern=r"^kontol$")
async def lumi(ganteng):
    await ganteng.reply(choice(lumimarah))
@register(incoming=True, from_users=LUMITED, pattern=r"^tes$")
async def tes(client, message: Message):
    await client.send_reaction(message.chat.id, message.id, "🎮")


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "devping": f"**Plugin:** `Perintah Ini Hanya Untuk Devs ʟᴜᴍɪᴇʀᴇ ᴜsᴇʀʙᴏᴛ.`\
        \n\n  »  **Perintah : **`Cping`\
        \n  »  **Notes :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
) 
