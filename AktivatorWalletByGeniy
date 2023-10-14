from pyrogram import Client, filters, enums
import sys
import asyncio

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(chatsid))
async def findchequecmd(client, message):
    if "Получить:" in message.reply_markup.inline_keyboard[0][0].text:
        if message.reply_markup.inline_keyboard[0][0].url.startswith("https://t.me/wallet?start="):
            code = message.reply_markup.inline_keyboard[0][0].url[26:]
            await app.send_message("wallet", f"/start {code}")
        #print(message.reply_markup.inline_keyboard[0][0].text)

@app.on_message(filters.chat("wallet"))
async def walletcmd(client, message):
    try:
        if "Вы не можете активировать этот чек, так как вы не являетесь подписчиком канала" in message.text:
            chatlink = message.reply_markup.inline_keyboard[0][0].url
            chequelink = message.reply_markup.inline_keyboard[1][0].url[26:]
            chequeusername = message.reply_markup.inline_keyboard[0][0].text
            await app.join_chat(chatlink)
            await app.send_message("wallet", f"/start {chequelink}")
            await asyncio.sleep(3600)
            await app.leave_chat(chequeusername)
    except:
        pass




@app.on_message(filters.command("stop", prefixes="."))
async def stopcmd(client, message):
    if message.from_user.id == userid:
        await app.send_message("me", "**Бот остановлен.**")
        await app.stop()
        sys.exit()








app.run()
