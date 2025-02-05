import telebot
from pyexpat.errors import messages
from telebot import types
import random





#Функция для выдачи событий
questions_events = {
    "Что произошло в 862 году?": {
        "answers": ["разгром «злого города» Козельска", "войска Батыя разгромили Рязань", "призвание варягов", "битва на реке Калка"],
        "correct": "призвание варягов"
    },
    "Что произошло в 882 году?": {
        "answers": ["поход Владимира Мономаха на половцев", "восстание древлян", "курултай на котором Тимучин был избран Чингизханом", "захват Олегом Киева, объединение Киева и Новгорода"],
        "correct": "захват Олегом Киева, объединение Киева и Новгорода"
    },
    "Что произошло в 907 году?": {
        "answers": ["поход князя Игоря Новгород-Северского на половцев", "установление республики в Киеве", "первый поход Олега на Царьград", "смерть Мстислава Великого и началась Раздробленность"],
        "correct": "первый поход Олега на Царьград"
    },
    "Что произошло в 911 году?": {
        "answers": ["подписание торгового договора Руси с Византией", "антиордынское восстание в Твери", "Любеческий съезд князей","битва на реке Шелони"],
        "correct": "подписание торгового договора Руси с Византией"
    },
    "Что произошло в 945 году?": {
        "answers": ["языческая реформа Владимира", "убийство Игоря Старого древлянами", "разгром войсками Батыя Владимира", "поход Владимира Мономаха на половцев"],
        "correct": "убийство Игоря Старого древлянами"
    },
    "Что произошло в 957 году?": {
        "answers": ["призвание варягов", "стояние на реке Угре", "крещение княгини Ольги в Константинополе","битва при Доростоле"],
        "correct": "крещение княгини Ольги в Константинополе"
    },
    "Что произошло в 980 году?": {
        "answers": ["присоединение Новгорода к Москве", "восстание в Киеве против ростовщиков", "поход Едигея на Москву","языческая реформа Владимира"],
        "correct": "языческая реформа Владимира"
    },
    "Что произошло в 988 году?": {
        "answers": ["крещение Руси", "набег Тохтамыша на Москву", "битва на реке Сити","поход Владимира Мономаха на половцев"],
        "correct": "крещение Руси"
    },
    "Что произошло в 1030 году?": {
        "answers": ["Ледовое побоище на Чудском озере", "основание города Юрьев (Тарту)", "разгром Киева войсками Батыя","установление республики в Новгороде"],
        "correct": "основание города Юрьев (Тарту)"
    },
    "Что произошло в 1068 году?": {
        "answers": ["Куликовская битва", "захват Олегом Киева", "битва на реке Альте","Грюнвальдская битва"],
        "correct": "битва на реке Альте"
    },
    "Что произошло в 1097 году?": {
        "answers": ["Невская битва", "крещение княгини Ольги в Константинополе", "битва на реке Воже","съезд князей в Любече"],
        "correct": "съезд князей в Любече"
    },
    "Что произошло в 1111 году?": {
        "answers": ["поход Владимира Мономаха на половцев", "нашествие «Неврюевой рати»", "присоединение Новгорода к Москве","языческая реформа Владимира"],
        "correct": "поход Владимира Мономаха на половцев"
    },
    "Что произошло в 1113 году?": {
        "answers": ["присоединение Коломны к Москве", "восстание в Киеве против ростовщиков", "первый поход Олега на Царьград","установление республики в Новгороде"],
        "correct": "восстание в Киеве против ростовщиков"
    },
    "Что произошло в 1147 году?": {
        "answers": ["разгром Киева войсками Андрея Боголюбского", "поход князя Игоря Новгород-Северского на половцев", "первое упоминание Москвы в летописи","войска Батыя разгромили Рязань"],
        "correct": "первое упоминание Москвы в летописи"
    },
    "Что произошло в 1136 году?": {
        "answers": ["смерть Мстислава Великого", "первое упоминание Москвы в летописи", "поход Владимира Мономаха на половцев","установление в городе республиканской формы правления"],
        "correct": "установление в городе республиканской формы правления"
    },
    "Что произошло в 1169 году?": {
        "answers": ["разгром Киева войсками Андрея Боголюбского", "Невская битва", "основание города Юрьев (Тарту)","разгром «злого города» Козельска"],
        "correct": "разгром Киева войсками Андрея Боголюбского"
    },
    "Что произошло в 1185 году?": {
        "answers": ["восстание в Киеве против ростовщиков", "поход князя Игоря Новгород-Северского в поход против половцев", "постройка Белокаменного кремля в Москве","битва на реке Калка"],
        "correct": "поход князя Игоря Новгород-Северского в поход против половцев"
    },
    "Что произошло в 1206 году?": {
        "answers": ["войска Батыя разгромили Рязань", "разгром Киева войсками Андрея Боголюбского", "курултай. избрание Чингисхана","на Москву пришла Дюденева рать"],
        "correct": "курултай. избрание Чингисхана"
    },
    "Что произошло в 1223 году?": {
        "answers": ["антиордынское восстание в Твери", "битва на реке Пьяне", "битва на реке Альте","битва на реке Калка"],
        "correct": "битва на реке Калка"
    },
    "Что произошло в 1237 году?": {
        "answers": ["разгром Батыем Рязани", "битва на реке Сити", "разгром войсками Батыя Владимира","разгром войсками Батыя Москвы"],
        "correct": "разгром Батыем Рязани"
    },
    "Что не произошло в 1238 году?": {
        "answers": ["битва на реке Сити", "разгром Киева войсками Батыя", "разгром войсками Батыя Владимира","разгром войсками Батыя Москвы"],
        "correct": "разгром Киева войсками Батыя"
    },
    "Что произошло в 1240 году?": {
        "answers": ["Объединение Галицкого и Волынского княжеств","Разгром «злого города» Козельска","Невская битва","Разгром Батыем Рязани"],
        "correct": "Невская битва"
    },
    "Что произошло в 1242 году?": {
        "answers": ["Ледовое побоище","Неврюева рать","битва на р. Сити","Битва на реке Калка"],
        "correct": "Ледовое побоище"
    },
    "Что произошло в 1293 году?": {
        "answers": ["Невская битва","Поход князя Игоря Новгород-Северского в поход против половцев ","Ледовое побоище на Чудском озере","Дюденева рать"],
        "correct": "Дюденева рать"
    },
    "Что произошло в 1301 году?": {
        "answers": ["Дюденева рать","Присоединение Коломны к Москве","Неврюева рать","Бортеневская битва"],
        "correct": "Присоединение Коломны к Москве"
    },
    "Что произошло в 1302 году?": {
        "answers": ["Антиордынское восстание в Твери","битва на р. Пьяне","Ледовое побоище на Чудском озере","Присоединение Переяславля к Москве"],
        "correct": "Присоединение Переяславля к Москве"
    },
    "Что произошло в 1327 году?": {
        "answers": ["Антиордынское восстание в Твери","Присоединение Коломны","Перенос митрополичьей кафедры в Москву","Бортеневская битва"],
        "correct": "Антиордынское восстание в Твери"
    },
    "Что произошло в 1328 году?": {
        "answers": ["постройка Белокаменного кремля в Москве","Куликовская битва","Кревская уния","Перенос митрополичьей кафедры из Владимира в Москву"],
        "correct": "Перенос митрополичьей кафедры из Владимира в Москву"
    },
    "Что началось в 1367 году?": {
        "answers": ["набег Тохтамыша на Москву","Строительство белокаменного Кремля в Москве","набег Едигея на Москву","Перенос митрополичьей кафедры в Москву"],
        "correct": "Строительство белокаменного Кремля в Москве"
    },
    "Что произошло в 1377 году?": {
        "answers": ["Кревская уния","Куликовская битва","постройка Белокаменного кремля в Москве","Битва на реке Пьяне"],
        "correct": "Битва на реке Пьяне"
    },
    "Что произошло в 1378 году?": {
        "answers": ["набег Тохтамыша на Москву","Битва на реке Воже","присоединение Нижнего Новгорода к Москве","Антиордынское восстание в Твери"],
        "correct": "Битва на реке Воже"
    },
    "Что произошло в 1380 году?": {
        "answers": ["передача ярлыка по наследству в завещании Донского","битва на р. Пьяне","битва на р. Воже","Куликовская битва"],
        "correct": "Куликовская битва"
    },
    "Что произошло в 1382 году?": {
        "answers": ["набег хана Тохтамыша на Москву","","",""],
        "correct": "набег хана Тохтамыша на Москву"
    },
    "Что произошло в 1392 году?": {
        "answers": ["Бортеневская битва","постройка Белокаменного кремля в Москве","Присоединение Нижнего Новгорода к Москве","Грюнвальдская битва"],
        "correct": "Присоединение Нижнего Новгорода к Москве"
    },
    "Что произошло в 1408 году?": {
        "answers": ["Набег хана Едигея на Москву","несостоявшееся нашествие Тамерлана","набег Тохтамыша на Москву","битва на р. Воже"],
        "correct": "Набег хана Едигея на Москву"
    },
    "Что произошло в 1410 году?": {
        "answers": ["несостоявшееся нашествие Тамерлана","Набег хана Едигея на Москву","Грюнвальдская битва","Присоединение Нижнего Новгорода к Москве"],
        "correct": "Грюнвальдская битва"
    },
    "Что произошло в 1448 году?": {
        "answers": ["Падение Византийской империи","Автокефалия РПЦ","присоединение Новгорода","присоединение Твери"],
        "correct": "Автокефалия РПЦ"
    },
    "Что произошло в 1453 году?": {
        "answers": ["Автокефалия РПЦ","Набег хана Едигея на Москву","Присоединение Нижнего Новгорода к Москве","Падение Византийской империи"],
        "correct": "Падение Византийской империи"
    },
    "Что произошло в 1463 году?": {
        "answers": ["присоединение Новгорода","Присоединение Ярославля","Бортеневская битва","Грюнвальдская битва"],
        "correct": "Присоединение Ярославля"
    },
    "Что произошло в 1471 году?": {
        "answers": ["битва на р. Шелони с Новгородом","присоединение Новгорода","Присоединение Ярославля","стояние на реке Угре"],
        "correct": "битва на р. Шелони с Новгородом"
    },
    "Что произошло в 1478 году?": {
        "answers": ["Падение Византийской империи","Набег хана Едигея на Москву","присоединение Новгорода","битва на р. Шелони с Новгородом"],
        "correct": "присоединение Новгорода"
    },
    "Что произошло в 1480 году?": {
        "answers": ["Автокефалия РПЦ","стояние на реке Угре","присоединение Новгорода","Грюнвальдская битва"],
        "correct": "стояние на реке Угре"
    },
    "Что произошло в 1485 году?": {
        "answers": ["битва на р. Шелони с Новгородом","Битва при Ведроши","присоединение Твери","стояние на реке Угре"],
        "correct": "присоединение Твери"
    },
    "Что произошло в 1497 году?": {
        "answers": ["издание Судебника Ивана III. Начало закрепощения","присоединение Пскова","присоединение Твери","присоединение Новгорода"],
        "correct": "издание Судебника Ивана III. Начало закрепощения"
    },
    "Что произошло в 1500 году?": {
        "answers": ["присоединение Твери","Битва при Ведроши","присоединение Смоленска","присоединение Рязани (окончание раздробленности)"],
        "correct": "Битва при Ведроши"
    },
    "Что произошло в 1510 году?": {
        "answers": ["стояние на реке Угре","присоединение Пскова","созыв первого Земского собора","присоединение Твери"],
        "correct": "присоединение Пскова"
    },
    "Что произошло в 1514 году?": {
        "answers": ["венчание Ивана Грозного на царство","присоединение Смоленска","присоединение Твери","созыв первого Земского собора"],
        "correct": "присоединение Смоленска"
    },
    "Что произошло в 1521 году?": {
        "answers": ["присоединение Рязани (окончание раздробленности)","Битва при Ведроши","присоединение Твери","присоединение Новгорода"],
        "correct": "присоединение Рязани (окончание раздробленности)"
    },
    "Что произошло в 1547 году?": {
        "answers": ["присоединение Твери","созыв первого Земского собора","Присоединение Ярославля","венчание Ивана Грозного на царство"],
        "correct": "венчание Ивана Грозного на царство"
    },
    "Что произошло в 1549 году?": {
        "answers": ["венчание Ивана Грозного на царство","созыв первого Земского собора","присоединение Смоленска","присоединение Твери"],
        "correct": "созыв первого Земского собора"
    },
    "Что произошло в 1550 году?": {
        "answers": ["венчание Ивана Грозного на царство", "Стоглавый собор", "присоединение Смоленска","издание Судебника Ивана Грозного"],
        "correct": "издание Судебника Ивана Грозного"
    },
    "Что также произошло в 1550 году?": {
        "answers": ["Стоглавый собор", "Присоединение Астрахани к России", "отмена кормлений","создание системы приказов"],
        "correct": "создание системы приказов"
    },
    "Что произошло в 1551 году?": {
        "answers": ["Стоглавый собор", "созыв первого Земского собора", "присоединение Пскова","отмена кормлений"],
        "correct": "Стоглавый собор"
    },
    "Что произошло в 1552 году?": {
        "answers": ["Присоединение Астрахани к России", "созыв первого Земского собора", "присоединение Казани к России. Постройка Свияжска","присоединение Рязани (окончание раздробленности)"],
        "correct": "присоединение Казани к России. Постройка Свияжска"
    },
    "Что произошло в 1556 году?": {
        "answers": ["Присоединение Астрахани к России", "издание Судебника Ивана Грозного", "Битва при Ведроши","Стоглавый собор"],
        "correct": "Присоединение Астрахани к России"
    },
    "Что также произошло в 1556 году?": {
        "answers": ["присоединение Казани к России. Постройка Свияжска", "Стоглавый собор", "венчание Ивана Грозного на царство","отмена кормлений. Появление выборных губных и земских старост"],
        "correct": "отмена кормлений. Появление выборных губных и земских старост"
    },
    "Что еще произошло в 1556 году?": {
        "answers": ["присоединение Казани к России. Постройка Свияжска", "битва при Чашниках", "создание системы приказов","Принятие «Уложения о службе»"],
        "correct": "Принятие «Уложения о службе»"
    },
    "Что произошло в 1564 году?": {
        "answers": ["Люблинская уния", "издание Судебника Ивана Грозного", "битва при Чашниках", "битва у села Молоди"],
        "correct": "битва при Чашниках"
    },
    "Что также произошло в 1564 году?": {
        "answers": ["Люблинская уния", "оборона Пскова от войск Стефана Батория", "Введение заповедных лет", "Начало книгопечатания на Руси"],
        "correct": "Начало книгопечатания на Руси"
    },
    "Что произошло в 1569 году?": {
        "answers": ["присоединение Казани к России. Постройка Свияжска", "Люблинская уния", "оборона Пскова от войск Стефана Батория", "Ям-Запольский мир с Речью Посполитой"],
        "correct": "Люблинская уния"
    },
    "Что произошло в 1572 году?": {
        "answers": ["битва у села Молоди", "Плюсское перемирие со Швецией", "венчание Ивана Грозного на царство", "Учреждение патриаршества"],
        "correct": "битва у села Молоди"
    },
    "Что произошло в 1581 году?": {
        "answers": ["Начало книгопечатания на Руси", "Присоединение Астрахани к России", "оборона Пскова от войск Стефана Батория ", "Стоглавый собор"],
        "correct": "оборона Пскова от войск Стефана Батория"
    },
    "Что еще произошло в 1581 году?": {
        "answers": ["смерть Дмитрия в Угличе", "Введение заповедных лет", "битва у села Молоди", "Ям-Запольский мир с Речью Посполитой"],
        "correct": "Введение заповедных лет"
    },
    "Что произошло в 1582 году?": {
        "answers": ["Плюсское перемирие со Швецией", "Учреждение патриаршества", "Ям-Запольский мир с Речью Посполитой", "смерть Дмитрия в Угличе"],
        "correct": "Ям-Запольский мир с Речью Посполитой"
    },
    "Что произошло в 1583 году?": {
        "answers": ["Тявзинский мир c Швецией", "Введение урочных лет", "оборона Пскова от войск Стефана Батория", "Плюсское перемирие со Швецией"],
        "correct": "Плюсское перемирие со Швецией"
    },
    "Что произошло в 1589 году?": {
        "answers": ["Введение урочных лет", "Учреждение патриаршества", "смерть Дмитрия в Угличе", "Введение заповедных лет"],
        "correct": "Учреждение патриаршества"
    },
    "Что произошло в 1591 году?": {
        "answers": ["Тявзинский мир c Швецией", "Введение урочных лет", "смерть Дмитрия в Угличе", "Учреждение патриаршества"],
        "correct": "смерть Дмитрия в Угличе"
    },
    "Что произошло в 1595 году?": {
        "answers": ["Введение урочных лет", "Учреждение патриаршества", "Введение заповедных лет", "Тявзинский мир c Швецией"],
        "correct": "Тявзинский мир c Швецией"
    },
    "Что произошло в 1597 году?": {
        "answers": ["Введение урочных лет", "Введение заповедных лет", "Ям-Запольский мир с Речью Посполитой", "битва у села Молоди"],
        "correct": "Введение урочных лет"
    },
}
# "Что произошло в 1549 году?": {
#         "answers": ["", "", "",""],
#         "correct": ""
#     }
def event_func (bot,message):
  question, data = random.choice(list(questions_events.items()))  # Изменено на questions_events
  answers_events = data["answers"]
  correct_answer_events = data["correct"]

  markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
  for answer in answers_events:
    markup.add(answer)

  bot.send_message(message.chat.id, question, reply_markup=markup)

  # Устанавливаем ожидание ответа от пользователя
  bot.register_next_step_handler(message, lambda msg: check_answer_event(bot,msg, correct_answer_events))


def check_answer_event(bot,message, correct_answer_events):
    if message.text == correct_answer_events:
      bot.send_message(message.chat.id, "Правильно! Молодец!")
      bot.send_message(message.chat.id, "Хотите продолжить? Напишите 'да' или 'нет'.")
      bot.register_next_step_handler(message, lambda msg: restart_event_or_not(bot, msg))
    else:
      bot.send_message(message.chat.id, f"Неправильно. Правильный ответ: {correct_answer_events}")
      bot.send_message(message.chat.id, "Хотите продолжить? Напишите 'да' или 'нет'.")
      bot.register_next_step_handler(message, lambda msg: restart_event_or_not(bot, msg))


def restart_event_or_not(bot,message):
    if message.text.lower() == 'да':
        event_func(bot,message)  # Возвращаемся к началу
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, "Хорошо, до свидания! Если передумаешь - используй /start")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, ответьте 'да' или 'нет'.")
        bot.register_next_step_handler(message, lambda msg: restart_event_or_not(bot, msg))
