import asyncio
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,                             InlineKeyboardMarkup, InputMediaPhoto, Message)


from SanskariRobot import pbot as bot
      
Iron_Men = "https://telegra.ph/file/0ae6fee38ff2f30243d82.jpg"  

@bot.on_message(filters.command(["noob", "owner"]))
async def repo(client, message):   
       await message.reply_photo(      
            photo=Iron_Men,      
            caption=f"""**ʜᴇʏ {message.from_user.mention()},\n\nɪ ᴀᴍ [「 𝐒𝐀𝐍𝐒𝐊𝐀𝐑𝐈𒆜 ʀᴏʙᴏᴛ 」](t.me/SanskariRobot)**
""",        
            reply_markup=InlineKeyboardMarkup(   
                  [          
                        [          
                              InlineKeyboardButton("• ᴏᴡɴᴇʀ •", url="https://t.me/DORAMONX"),        
                              
                        ]     
                  ]      
            ),     
      )
      
       
        
         

              
                
                      
                      
                        
                          
             

                                       
                                        
__mod_name__ = "Oᴡɴᴇʀ" 

