import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SanskariRobot.events import register
from SanskariRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/ef1862c4e9a3271fd725f.jpg",
    "https://telegra.ph/file/ef1862c4e9a3271fd725f.jpg",
]


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ 「 𝐒𝐀𝐍𝐒𝐊𝐀𝐑𝐈 𒆜 ʀᴏʙᴏᴛ 」​**\n━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ᴅᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/DORAMONX)** \n\n"
    TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n"
    TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━\n\n"
    BUTTON = [
        [
            Button.url("ʜᴇʟᴘ​", "https://t.me/@SANSKARI_CHATTERBOX?start=help"),
            Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/@SANSKARI_CHATTERBOX"),
        ]
    ]
    ran = random.choice(PHOTO)
    await tbot.send_file(event.chat_id, ran, caption=TEXT, buttons=BUTTON)


## Alive mod
