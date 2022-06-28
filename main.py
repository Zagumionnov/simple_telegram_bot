"""simple echo telegram bot"""

import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Random number")
    item2 = types.KeyboardButton("How are you?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Welcome, {0.first_name}!".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Random number':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'How are you?':
            bot.send_message(message.chat.id, 'Oh gush, all kinds  of stuff! How are you?')
        else:
            bot.send_message(message.chat.id, 'I can\'t answer you :(')


# run
bot.polling(none_stop=True)
