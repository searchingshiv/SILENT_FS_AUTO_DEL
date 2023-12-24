import asyncio
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64
from configs import Config

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_ids=file_id)

    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await media_forward(bot, user_id, file_id)

async def send_media_and_reply(bot: Client, user_id: int, file_id: int, message: Message):
    sent_message = await media_forward(bot, user_id, file_id)
    text = await bot.send_message(message.chat.id, "[𝐅𝐢𝐥𝐞𝐬 𝐰𝐢𝐥𝐥 𝐛𝐞 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐢𝐧 𝟑𝟎 𝐦𝐢𝐧𝐮𝐭𝐞𝐬](https://telegram.me/The_Silent_Teams)", disable_web_page_preview=True)
    asyncio.create_task(delete_after_delay(sent_message, 60, text))

async def delete_after_delay(message, delay, text):
    await asyncio.sleep(delay)
    await message.delete()
    await text.delete()
