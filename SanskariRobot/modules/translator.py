from emoji import UNICODE_EMOJI
from telegram import Update, ParseMode
from telegram.ext import CallbackContext
from gpytranslate import SyncTranslator
from SanskariRobot import dispatcher
from SanskariRobot.modules.disable import DisableAbleCommandHandler

trans = SyncTranslator()


def totranslate(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    reply_msg = message.reply_to_message
    if not reply_msg:
        message.reply_text(
           "Rᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇs ᴏʀ ᴡʀɪᴛᴇ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴏᴛʜᴇʀ ʟᴀɴɢᴜᴀɢᴇs ​​ғᴏʀ ᴛʀᴀɴsʟᴀᴛɪɴɢ ɪɴᴛᴏ ᴛʜᴇ ɪɴᴛᴇɴᴅᴇᴅ ʟᴀɴɢᴜᴀɢᴇ\n\n"
            "Exᴀᴍᴘʟᴇ: `/tr  ᴇɴ-ʜɪ` ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ғʀᴏᴍ Eɴɢʟɪsʜ ᴛᴏ Hɪɴᴅɪ\n" 
            "Oʀ ᴜsᴇ: `/tr ᴇɴ` ғᴏʀ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴅᴇᴛᴇᴄᴛɪᴏɴ ᴀɴᴅ ᴛʀᴀɴsʟᴀᴛɪɴɢ ɪᴛ ɪɴᴛᴏ ᴇɴɢʟɪsʜ.\n" 
            "Cʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ sᴇᴇ [Lɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ Lᴀɴɢᴜᴀɢᴇ Cᴏᴅᴇs](https://telegra.ph/ɪᴛs-ᴍᴇ-𒆜-𝐒𝐀𝐍𝐒𝐊𝐀𝐑𝐈-06-15).",
            parse_mode="markdown",
            disable_web_page_preview=True,
        )
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = trans.detect(to_translate)
            dest = args
    except IndexError:
        source = trans.detect(to_translate)
        dest = "en"
    translation = trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"<b>ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} ᴛᴏ {dest}</b> :\n"
        f"<code>{translation.text}</code>"
    )

    message.reply_text(reply, parse_mode=ParseMode.HTML)



__mod_name__ = "Tʀᴀɴsʟᴀᴛᴏʀ"

TRANSLATE_HANDLER = DisableAbleCommandHandler(["tr", "tl"], totranslate)

dispatcher.add_handler(TRANSLATE_HANDLER)

__command_list__ = ["tr", "tl"]
__handlers__ = [TRANSLATE_HANDLER]
