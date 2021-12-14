import telebot

f = open('config.txt', 'r')
data = f.read()
token, father_id = data.split()
bot = telebot.TeleBot(token, threaded=False)

bot.send_message(father_id, 'Hello, father')
