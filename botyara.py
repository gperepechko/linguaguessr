import telebot
from keys import token
from telebot import types
from game import Game
DEBUG = True

games = dict()
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Welcome to Linguaguessr! I am thinking of a certain language. Can you guess which one it is?\n" +
    "Send me 'Begin' to start a new game")
    global games
    games[message.chat.id] = Game(debug=DEBUG)

@bot.message_handler(content_types='text')
def message_reply(message):
    global games
    try:
        g = games[message.chat.id]
    except KeyError:
        bot.send_message(message.chat.id,"To start the game send /start")
        print('User plays without /start') 
        return
    if message.text=="Begin":
        bot.send_message(message.chat.id,"Game has started")
        bot.send_message(message.chat.id,"Make a guess")
        games[message.chat.id] = Game(debug=DEBUG)
        return
    if message.text=="End":
        bot.send_message(message.chat.id,"Game has stopped")
        bot.send_message(message.chat.id,"Correct language: " + g.language)
        return
    status = g.make_guess(message.text)
    if not status:
        bot.send_message(message.chat.id,"I don't know such language")
        return
    bot.send_message(message.chat.id,status)
bot.infinity_polling()
