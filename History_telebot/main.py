from gc import callbacks
import random
import telebot
from pyexpat.errors import messages
from telebot import types
from data_check import data_func, check_answer,restart_or_not
from event_check import event_func,check_answer_event,restart_event_or_not
from information import info_about



with open ('token.txt', 'r', encoding='UTF-8') as file:
     Bot_token = file.read()

bot = telebot.TeleBot(Bot_token)

@bot.message_handler(commands = ['start', 'menu'])
def start(message):
  bot.send_message(message.chat.id, 'Привет-привет! Это бот поможет тебе выучить даты по истории России')
  markup = types.InlineKeyboardMarkup()
  button1 = types.InlineKeyboardButton ('Повторять даты событий', callback_data = 'dates')
  button2 = types.InlineKeyboardButton ('Повторять события по датам', callback_data = 'events')
  button3 = types.InlineKeyboardButton ('Открыть сайт с датами', callback_data = 'site')
  button4 = types.InlineKeyboardButton ('Информация', callback_data = 'info')
  markup.add(button1)
  markup.add(button2)
  markup.add(button3)
  markup.add(button4)
  bot.send_message(message.chat.id, 'Вот основные кнопки', reply_markup= markup)

#Отправка на сайт с датами
@bot.message_handler(commands=['site', 'website'])
def site (message):
  bot.send_message(message.chat.id, 'Хорошо, сейчас я скину ссылку на сайт с датами для подготовки')
  bot.send_message(message.chat.id,'https://vpr-ege.ru/ege/istoriya/2038-daty-dlya-ege-po-istorii?ysclid=m2rc63qbhi806744659')

#Получение файлов с неправильным форматом
@bot.message_handler(content_types= ['audio', 'video', 'photo', 'document', 'voice', 'video_note', 'location', 'contact',
'sticker','poll', 'dice'])
def get_error_files (message):
  bot.send_message(message.chat.id, 'Перестань, пожалуйста, присылать мне всякую хуйню и воспользуйся кнопками или командами (/)')

#Обработка нажатий на кнопки:
@bot.callback_query_handler(func = lambda callback:True)
def callback_message (callback):
    bot.answer_callback_query(callback.id)
    if callback.data == 'site':
      bot.send_message(callback.message.chat.id, 'Хорошо, сейчас я скину ссылку на сайт с датами для подготовки')
      bot.send_message(callback.message.chat.id, 'https://vpr-ege.ru/ege/istoriya/2038-daty-dlya-ege-po-istorii?ysclid=m2rc63qbhi806744659')
    elif callback.data == 'dates':
      data_func(bot,callback.message.chat.id)
    elif callback.data == 'events':
      event_func (bot,callback.message)
    elif callback.data == 'info':
      info_about(bot,callback.message)









if __name__ == "__main__":
    bot.polling(none_stop = True)
