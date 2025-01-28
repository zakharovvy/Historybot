import random
import pprint
from telebot import TeleBot


def data_func (bot,chat_id):
  rand_data = random.randint(1,100)
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
    case 48:
      question = 'В каком году произошло присоединение Твери к Московскому княжеству?'
      correct_answer = '1485'
    case 49:
      question = 'В каком году произошло издание Судебника Ивана III?'
      correct_answer = '1497'
    case 50:
      question = 'В каком году произошла Битва при Ведроши?'
      correct_answer = '1503'
    case 51:
      question = 'В каком году произошло осуждение взглядов нестяжателей?'
      correct_answer = '1503'
    case 52:
      question = 'В каком году произошло присоединение Пскова к Московскому княжеству?'
      correct_answer = '1510'
    case 53:
      question = 'В каком году произошло присоединение Смоленска к Московскому княжеству'
      correct_answer = ''
    case 54:
      question = 'В каком году произошло присоединение Рязани?'
      correct_answer = '1521'
    case 55:
      question = 'В каком году произошло венчание Ивана Грозного на царство'
      correct_answer = '1547'
    case 56:
      question = 'В каком году произошел созыв первого Земского собора?'
      correct_answer = '1549'
    case 57:
      question = 'В каком году произошло издание Судебника Ивана Грозного?'
      correct_answer = '1550'
    case 58:
      question = 'В каком году произошел Стоглавый собор?'
      correct_answer = '1551'
    case 59:
      question = 'В каком году произошло присоединение Казани к России?'
      correct_answer = '1552'
    case 60:
      question = 'В каком году произошло присоединение Астрахани к России?'
      correct_answer = '1556'
    case 61:
      question = 'В каком году произошло принятие «Уложения о службе»?'
      correct_answer = '1556'
    case 62:
      question = 'В каком году произошла битва при Чашниках?'
      correct_answer = '1564'
    case 63:
      question = 'В каком году началось книгопечатания на Руси ("Апостол")'
      correct_answer = '1564'
    case 64:
      question = 'В каком году произошла Люблинская уния об объединении Польши с Литвой?'
      correct_answer = '1569'
    case 65:
      question = 'В каком году произошла битва у села Молоди?'
      correct_answer = '1572'
    case 66:
      question = 'В каком году произошло разорение Москвы Дивлет-Гиреем?'
      correct_answer = '1571'
    case 67:
      question = 'В каком году произошла оборона Пскова от войск Стефана Батория?'
      correct_answer = '1581'
    case 68:
      question = 'В каком году был заключен Ям-Запольский мир с Речью Посполитой?'
      correct_answer = '1582'
    case 69:
      question = 'В каком году было заключено Плюсское перемирие со Швецией?'
      correct_answer = '1583'
    case 70:
      question = 'В каком году произошло учреждение патриаршества в России?'
      correct_answer = '1589'
    case 71:
      question = 'В каком году произошла смерть Дмитрия Ивановича в Угличе?'
      correct_answer = '1591'
    case 72:
      question = 'В каком году был заключен Тявзинский мир со Швецией?'
      correct_answer = '1595'
    case 73:
      question = 'В каком году произошло введение урочных лет?'
      correct_answer = '1597'
    case 74:
      question = 'В каком году произошло избрание на царство Бориса Годунова?'
      correct_answer = '1598'
    case 75:
      question = 'В каком году произошла битва при Добрыничах?'
      correct_answer = '1605'
    case 76:
      question = 'В каком году произошла битва под Болховым?'
      correct_answer = '1608'
    case 77:
      question = 'В каком году был заключен Выборгский договор со Швецией?'
      correct_answer = '1609'
    case 78:
      question = 'В каком году произошла битва при Клушине?'
      correct_answer = '1610'
    case 79:
      question = 'В каком году произошло освобождение Москвы от польско-литовских интервентов?'
      correct_answer = '1612'
    case 80:
      question = 'В каком году произошло избрание на престол Михаила Федоровича Романова?'
      correct_answer = '1613'
    case 81:
      question = 'В каком году был заключен Столбовский мир со Швецией?'
      correct_answer = '1617'
    case 82:
      question = 'В каком году произошло заключение Деулинское перемирие с Польшей?'
      correct_answer = '1618'
    case 83:
      question = 'В каком году начался выпуск рукописной газеты Куранты?'
      correct_answer = '1621'
    case 84:
      question = 'В каком году произошел Соляной бунт?'
      correct_answer = '1648'
    case 85:
      question = 'В каком году произошла битва под Желтыми водами?'
      correct_answer = '1648'
    case 86:
      question = 'В каком году было издано Соборное уложение?'
      correct_answer = '1649'
    case 87:
      question = 'В каком году произошли Хлебные бунты в Новгороде и Пскове?'
      correct_answer = '1650'
    case 88:
      question = 'В каком году произошла Переяславльская Рада?'
      correct_answer = '1654'
    case 89:
      question = 'В каком году произошло подписание Андрусовского перемирия Ординым-Нащокиным?'
      correct_answer = '1667'
    case 90:
      question = 'В каком году произошло создание приказа тайных дел?'
      correct_answer = '1654'
    case 91:
      question = 'В каком году был заключен Кардисский мир с Швецией?'
      correct_answer = '1661'
    case 92:
      question = 'В каком году произошел Медный бунт?'
      correct_answer = '1662'
    case 93:
      question = 'В каком году был принят Новоторговый устав?'
      correct_answer = '1667'
    case 94:
      question = 'В каком году произошла отмена местничества?'
      correct_answer = '1682'
    case 95:
      question = 'В каком году произошел стрелецкий бунт. т.н. "Хованщина"?'
      correct_answer = '1682'
    case 96:
      question = 'В каком году был заключен «Вечный мир» с Польшей?'
      correct_answer = '1686'
    case 97:
      question = 'В каком году произошло открытие Славяно-греко-латинской академии?'
      correct_answer = '1687'
    case 98:
      question = 'В каком году произошло подписание Нерчинского договор с Китаем?'
      correct_answer = '1689'
    case 99:
      question = 'В каком году произошел Первый Азовский поход?'
      correct_answer = '1695'
    case 100:
      question = 'В каком году произошла Второй Азовский поход?'
      correct_answer = '1696'


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



