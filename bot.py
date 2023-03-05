import telebot
from telebot import types

bot = telebot.TeleBot(int(os.environ.get["BOT_TOKEN"]))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'👋 Hello, This Bot Help you To Delete Service Messages In Groups/Channels.just add Me To Your group Or Channel As Admin With Delete Messages Permission')

@bot.message_handler(content_types=['service'])
def delete_service_messages(message):
    bot.delete_message(message.chat.id, message.message_id)

bot.polling()
