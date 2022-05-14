import telebot
from keys import token
from telebot import types
from game import Game
g = Game(debug=True)

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Welcome to Linguaguessr! I am thinking of a certain language. Can you guess which one it is?\n" +
    "Send me 'Begin' to start a new game")

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Start")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    # markup = types.ReplyKeyboardMarkup(row_width=2)
    # itembtn1 = types.KeyboardButton('a')
    # itembtn2 = types.KeyboardButton('v')
    # markup.add(itembtn1, itembtn2)
    # tb.send_message(chat_id, "Choose one letter:", reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    global g
    if message.text=="Begin":
        bot.send_message(message.chat.id,"Game has started")
        bot.send_message(message.chat.id,"Make a guess")
        g = Game(debug=True)
        return
    if message.text=="End":
        bot.send_message(message.chat.id,"Game has stopped")
        bot.send_message(message.chat.id,"Correct language: " + g.language)
        return
    status = g.make_guess(message.text)
    if not status:
        bot.send_message(message.chat.id,"This language does not exist")
        return
    bot.send_message(message.chat.id,status)
bot.infinity_polling()
