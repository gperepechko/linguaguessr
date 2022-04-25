import telebot
bot = telebot.TeleBot('5294129722:AAGFYo3vV846dMfuLYF_s1VrWmkI-IrZTgA')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome to Linguaguessr! I am thinking of a certain language. Can you guess which one it is?')

bot.polling()
