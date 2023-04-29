import telebot
from telebot import types

bot = telebot.TeleBot('5642518557:AAEjmLeECYLvz-Ql7b99F6EYCX2JhTqrbzA')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Hello  {message.from_user.first_name}</b>  <u>enter command /time</u>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['time'])
def look_time(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Irkutsk: go to website', url='https://www.timeserver.ru/cities/ru/irkutsk'))
    markup.add(types.InlineKeyboardButton('Auckland: go to website', url='https://time.is/ru/Auckland'))
    bot.send_message(message.chat.id, "Let's go", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def ending(message):
    bot.send_message(message.chat.id, f'<b>{message.from_user.first_name} thanks for using our bot </b>', parse_mode='html')



bot.polling(none_stop=True)