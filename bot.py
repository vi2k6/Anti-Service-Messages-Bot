import os
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# create a Pyrogram client
app = Client(
    "Anti-Service-Messages-Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH"),
    )

@app.on_message(filters.text)
def start_command(client, message):
    # send a message to the user who initiated the command
    client.send_message(chat_id=message.chat.id, text="Hello, I can delete all service messages in groups/channels.Just Add Me To Your Group/Channel!"),
    reply_markup=InlineKeyboardButton([[InlineKeyboardButton("Updates", url="https://myownbots.t.me")]])

@app.on_message(filters.service)
def delete_service_messages(client, message):
    try:
        client.delete_messages(chat_id=message.chat.id, message_ids=message.id)
    except ChatAdminRequired:
        print("I am not an admin in this group!")

app.run()
