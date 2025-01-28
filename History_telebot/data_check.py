import random
import pprint
from telebot import TeleBot


def data_func (bot,chat_id):
  rand_data = random.randint(1,47)
  match rand_data:
    case 1:
      question = 'В каком году произошло призвание варягов?'
      correct_answer = '862'
    case 2:
      question = 'В каком году произошел захват Олегом Киева, объединение Киева и Новгорода?'
      correct_answer = '882'
    case 3:
      question = 'В каком году произошел первый поход Олега на Царьград?'
      correct_answer = '907'
    case 4:
      question = 'В каком году произошло восстание древлян?'
      correct_answer = '945'
    case 5:
      question = 'В каком году произошло крещение княгини Ольги в Константинополе?'
      correct_answer = '957'
    case 6:
      question = 'В каком году произошла битва при Доростоле?'
      correct_answer = '971'
    case 7:
      question = 'В каком году произошла языческая реформа Владимира?'
      correct_answer = '980'
    case 8:
      question = 'В каком году произошло крещение Руси?'
      correct_answer = '988'
    case 9:
      question = 'В каком году произошла битва на реке Альте?'
      correct_answer = '1068'
    case 11:
      question = 'В каком году произошел Любеческий съезд князей?'
      correct_answer = '1097'
    case 12:
      question = 'В каком году произошло основание города Юрьев (Тарту)?'
      correct_answer = '1030'
    case 13:
      question = 'В каком году произошло восстание в Киеве против ростовщиков?'
      correct_answer = '1113'
    case 14:
      question = 'В каком году произошел поход Владимира Мономаха на половцев?'
      correct_answer = '1111'
    case 15:
      question = 'В каком году произошла смерть Мстислава Великого и началась Раздробленность?'
      correct_answer = '1132'
    case 16:
      question = 'В каком году произошло установление республики в Новгороде?'
      correct_answer = '1136'
    case 17:
      question = 'В каком году произошло первое упоминание Москвы в летописи?'
      correct_answer = '1147'
    case 18:
      question = 'В каком году произошел разгром Киева войсками Андрея Боголюбского?'
      correct_answer = '1169'
    case 19:
      question = 'В каком году произошел поход князя Игоря Новгород-Северского на половцев?'
      correct_answer = '1185'
    case 10:
      question = 'В каком году произошел курултай на котором Тимучин был избран Чингизханом?'
      correct_answer = '1206'
    case 21:
      question = 'В каком году произошла битва на реке Калка?'
      correct_answer = '1223'
    case 22:
      question = 'В каком году произошло присоединение Твери к Москве?'
      correct_answer = '1485'
    case 23:
      question = 'В каком году войска Батыя разгромили Рязань?'
      correct_answer = '1237'
    case 24:
      question = 'В каком году произошел разгром войсками Батыя Коломны, Москвы, Владимира?'
      correct_answer = '1238'
    case 25:
      question = 'В каком году произошла битва на р. Сити, смерть Юрия Всеволодовича и разгром его войска?'
      correct_answer = '1238'
    case 26:
      question = 'В каком году произошел разгром «злого города» Козельска?'
      correct_answer = '1238'
    case 27:
      question = 'В каком году произошел разгром Киева войсками Батыя и пленение Дмитра?'
      correct_answer = '1240'
    case 28:
      question = 'В каком году пришла «Неврюева рать», произошло смещение князя Андрея Ярославича и передача ярлыка на Владимирское княжество Александру Невскому?'
      correct_answer = '1253'
    case 29:
      question = 'В каком году произошла Невская битва?'
      correct_answer = '1240'
    case 30:
      question = 'В каком году произошло Ледовое побоище на Чудском озере?'
      correct_answer = '1242'
    case 31:
      question = 'В каком году на Москву пришла Дюденева рать?'
      correct_answer = '1293'
    case 32:
      question = 'В каком году произошло присоединение Коломны к Москве?'
      correct_answer = '1301'
    case 33:
      question = 'В каком году произошло присоединение Переяславля к Москве?'
      correct_answer = '1302'
    case 34:
      question = 'В каком году произошло антиордынское восстание в Твери?'
      correct_answer = '1327'
    case 35:
      question = 'В каком году произошел перенос митрополичьей кафедры в Москву?'
      correct_answer = '1328'
    case 36:
      question = 'В каком году закончилась постройка Белокаменного кремля в Москве?'
      correct_answer = '1367'
    case 37:
      question = 'В каком году произошла битва на реке Пьяне?'
      correct_answer = '1377'
    case 38:
      question = 'В каком году произошла битва на реке Воже?'
      correct_answer = '1378'
    case 39:
      question = 'В каком году произошел набег Тохтамыша на Москву?'
      correct_answer = '1382'
    case 40:
      question = 'В каком году произошла Куликовская битва?'
      correct_answer = '1380'
    case 41:
      question = 'В каком году произошло присоединение Нижнего Новгорода к Москве?'
      correct_answer = '1392'
    case 42:
      question = 'В каком году произошел поход Едигея на Москву?'
      correct_answer = '1408'
    case 43:
      question = 'В каком году произошла Грюнвальдская битва?'
      correct_answer = '1410'
    case 44:
      question = 'В каком году произошла Флорентийская уния?'
      correct_answer = '1439'
    case 45:
      question = 'В каком году произошла битва на реке Шелони с Новгородом?'
      correct_answer = '1471'
    case 46:
      question = 'В каком году произошло присоединение Новгорода к Москве?'
      correct_answer = '1478'
    case 47:
      question = 'В каком году произошло Стояние на реке Угре?'
      correct_answer = '1480'

  bot.send_message(chat_id, question)

  bot.register_next_step_handler_by_chat_id(chat_id, lambda message: check_answer(bot,message, correct_answer))

#Функция для проверки корректности ответа
def check_answer(bot,message, correct_answer):
  if message.text == correct_answer:
        bot.send_message(message.chat.id, "Правильно! Молодец!")
  else:
        bot.send_message(message.chat.id, f"Неправильно. Правильный ответ: {correct_answer}")

  bot.send_message(message.chat.id, "Хотите продолжить? Напишите 'да' или 'нет'.")
  bot.register_next_step_handler(message, lambda msg: restart_or_not(bot, msg))

def restart_or_not(bot,message):
    if message.text.lower() == 'да':
        data_func (bot,message.chat.id)  # Возвращаемся к началу
    else:
        bot.send_message(message.chat.id, "Хорошо, до свидания! Если передумаешь - используй /start")



