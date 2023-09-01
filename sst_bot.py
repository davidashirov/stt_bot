import telebot

API_TOKEN = '6465220215:AAFuZj-ZSrj3KbLYLG3MNSv9uwA4QuwRSUc'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(content_types=['text'])
def echo_text(message):
    bot.send_message(message.chat.id, 'Получено')

bot.infinity_polling()

