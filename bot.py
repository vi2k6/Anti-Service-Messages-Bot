import os
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired

# create a Pyrogram client
app = Client(
    "Anti-Service-Messages-Bot",
    api_id=int(os.environ.get["API_ID"]),
    api_hash=os.environ.get["API_HASH"],
    bot_token=os.environ.get["BOT_TOKEN"]
    )

# define a function to send a message when a user sends /start command
@app.on_message(filters.command(["start"]))
def start_command(client, message):
    # send a message to the user who initiated the command
    client.send_message(chat_id=message.chat.id, text="Hello, Nice To Meet You!")

# define a function to delete service messages in groups
@app.on_message(filters.service)
def delete_service_messages(client, message):
    try:
        # delete the service message
        client.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)
    except ChatAdminRequired:
        # if the bot is not an admin in the group, catch the error and print a message
        print("I am not an admin in this group!")

# start the Pyrogram client
app.run()
