from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from SanskariRobot import pbot as client


ANON = "https://telegra.ph/file/0ae6fee38ff2f30243d82.jpg"


@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 𝐒𝐀𝐍𝐒𝐊𝐀𝐑𝐈 𒆜 ʀᴏʙᴏᴛ 」](t.me/SanskariRobot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [ᴅᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id=5301059277)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**「 𝐒𝐀𝐍𝐒𝐊𝐀𝐑𝐈 𒆜 ʀᴏʙᴏᴛ 」 sᴏᴜʀᴄᴇ ɪs ɴᴏᴡ ᴩᴜʙʟɪᴄ ᴀɴᴅ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://DORAMONX"),
                    InlineKeyboardButton(
                        "ʀᴏʙᴏᴛ",
                        url="https://github.com/Devil3420/𝐒𝐀𝐍𝐒𝐊𝐀𝐑𝐈Management"),
                      
                     
                    
                ]
            ]
        ),
    )


__mod_name__ = "Rᴇᴩᴏ"
