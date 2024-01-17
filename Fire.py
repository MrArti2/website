from pyrogram import Client
import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions

import requests

@app.on_message()
async def type(_,message):

        if "+fire" in message.text.lower():
                ms=message.text.lower()

                await asyncio.sleep(1)
                try:
                        m = await app.get_discussion_message(message.chat.id , message.id)

                        if "Пон, не попал" in ms:
                                await m.reply("+")
                        elif "+fire" in ms or "напиш" in ms:
                                await m.reply("Не попал")        
                except:
                        None



print("ok")
app.run()