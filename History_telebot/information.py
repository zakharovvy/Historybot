import telebot
from pyexpat.errors import messages
from telebot import types

def info_about(bot,message):
    with open('Date_of_payment', 'r',encoding='UTF8') as file:
        money_date = file.read()
    bot.send_message(message.chat.id,f'Данные бот работает на некоммерческой основе. '
                                     f'Все права защищены. \n Бот работает за счет пожертвований.'
                                     f'На данный момент работа бота оплачена до {money_date}.\n '
                                     f'Если вы хотите поддержать бота, то скиньте сколько не жалко'
                                     f'на карту. \n Номер карты: 5469380066017541 (Сбербанк) \n'
                                     f'Все полученные деньги пойдут не в карман кому-то, а'
                                     f' на оплату работы бота')
