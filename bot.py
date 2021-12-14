import telebot

with open('config.txt', 'r') as f:
    data = f.read()
token, father_id = data.split()
try:
    with open('bot_buffer.txt', 'r') as f:
        data = f.read()
        num_of_failed_tests = len(data.split('\n')) - 1
except FileNotFoundError:
    data = ''
    
if len(data) == 0:
    message = 'Все в порядке'
else:
    message = f'number of failed tests {num_of_failed_tests}\n' + data


bot = telebot.TeleBot(token, threaded=False)
bot.send_message(father_id, message)

with open('bot_buffer.txt', 'w') as f:
    f.write('')