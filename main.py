from pyrogram import Client, filters
import time
from config import api_id, api_hash, content_type, sent_text, sticker_id, after_next_sl>

pyro_client = Client("Active_account", api_id=api_id, api_hash=api_hash)

async def send_sticker(client, chat_id, sticker_id):
    await client.send_sticker(chat_id, sticker_id)

async def send_next(client, chat_id):
    await client.send_message(chat_id, '/next') #При использовании других ботов можно и>

@pyro_client.on_message(filters.private & filters.text)
async def my_event_handler(client, message):
    if ' Partner found ' in message.text: #Тут тоже самое, если нужна реакция не на это>
        if content_type == 'text':
            await message.reply_text(sent_text)
        elif content_type == 'sticker':
                await send_sticker(client, message.chat.id, sticker_id)

        time.sleep(before_next_sleep)

        await send_next(client, message.chat.id)

        time.sleep(after_next_sleep)

pyro_client.run()

