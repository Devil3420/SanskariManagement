from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os, re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from SanskariRobot import telethn as bot
from SanskariRobot import telethn as tgbot
from SanskariRobot.events import register
from SanskariRobot import dispatcher


edit_time = 5
""" =======================Iron_Men ROBOT====================== """
file1 = "https://telegra.ph/file/3679711c9600937ec1333.jpg"
file2 = "https://telegra.ph/file/5574df162dc40406b7ca1.jpg"
file3 = "https://telegra.ph/file/35cfb3b4260a47c05d5c1.mp4"
file4 = "https://telegra.ph/file/ef1862c4e9a3271fd725f.jpg"
file5 = "https://telegra.ph/file/0ae6fee38ff2f30243d82.jpg"
""" =======================Iron_Men ROBOT====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"ʜᴇʏ  {firstname}, \n Cʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ  \n ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ʏᴏᴜ ",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "Pᴏᴡᴇʀᴅ ʙʏ Aʙɪsʜɴᴏɪ  \n\n"
        LILIE += f"ғɪʀsᴛ ɴᴀᴍᴇ  : {PRO.first_name} \n"
        LILIE += f"ʟᴀsᴛ ɴᴀᴍᴇ  : {PRO.last_name}\n"
        LILIE += f"ʏᴏᴜ ʙᴏᴛ  : {PRO.bot} \n"
        LILIE += f"ʀᴇsᴛɪᴄᴛᴇᴅ  : {PRO.restricted} \n"
        LILIE += f"ʏᴏᴜʀ ɪᴅ  : {boy}\n"
        LILIE += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
