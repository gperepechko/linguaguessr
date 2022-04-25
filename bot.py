import telebot

bot = telebot.TeleBot('')

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome to Linguaguessr! I am thinking of a certain language. Can you guess which one it is?')

@bot.message_handler(content_types = ['text'])
def send_text(text):
    if text in 

bot.polling()
