from config import Config
from pyrogram import Client, filters

tgbot = Client(
  bot_token=Config.BOT_TOKEN,
  api_id=Config.API_ID,
  api_hash=Config.API_HASH,
  )


service_filter = filters.service


# function to send message
async def send_message(client, chat_id):
    await client.send_message(chat_id, "Hello, Thanks For Adding Me to group.\n\n Now Make me Admin With <b>Delete Messages</b> Permission")

# function to handle bot added to a group
@tgbot.on_message(filters.new_chat_members)
async def welcome(client, message):
    for member in message.new_chat_members:
        if member.id == client.get_me().id:
            await send_message(client, message.chat.id)

@tgbot.on_message(filters.text)
def start(client, message):
    client.send_message(message.chat.id, "Hi, This is a anti service bot.Just Add Me To Your Group By [Clicking Here](http://t.me/{Config.BOT_USERNAME}?startgroup=botstart) Then I Will delete all berfore and after service messages in the group.")

@tgbot.on_message(service_filter)
async def delete_service_message(client, message):
    # Delete service message
    await client.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)

tgbot.run()
