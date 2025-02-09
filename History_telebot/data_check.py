import random
import pprint
from telebot import TeleBot


def data_func (bot,chat_id):
    rand_data = random.randint(1,196)
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
          question = 'В каком году произошел Второй Азовский поход?'
          correct_answer = '1696'
        case 101:
          question = 'В каком году произошло введение юлианского календаря?'
          correct_answer = '1700'
        case 102:
          question = 'В каком году произошла Нарвская конфузия?'
          correct_answer = '1700'
        case 103:
          question = 'В каком году произошло издание первой регулярной печатной газеты «Ведомости»?'
          correct_answer = '1702'
        case 104:
          question = 'В каком году произошл основание Санкт-Петербурга?'
          correct_answer = '1703'
        case 105:
          question = 'В каком году произошла битва у деревни Лесной?'
          correct_answer = '1708'
        case 106:
          question = 'В каком году произошла Полтавская битва?'
          correct_answer = '1709'
        case 107:
          question = 'В каком году произошло создание Правительствующего Сената?'
          correct_answer = '1711'
        case 108:
          question = 'В каком году произошел Прутский поход?'
          correct_answer = '1711'
        case 109:
          question = 'В каком году произошел перенос столицы из Москвы в Петербург?'
          correct_answer = '1712'
        case 110:
          question = 'В каком году произошло издание Указа о единонаследии?'
          correct_answer = '1714'
        case 111:
          question = 'В каком году произошло Гангутское сражение?'
          correct_answer = '1714'
        case 112:
          question = 'В каком году произошло учреждение коллегий?'
          correct_answer = '1718'
        case 113:
          question = 'В каком году произошло Гренгамское сражение?'
          correct_answer = '1720'
        case 114:
          question = 'В каком году произошло учреждение Синода?'
          correct_answer = '1721'
        case 115:
          question = 'В каком году был заключен Ништадтский мирный договор?'
          correct_answer = '1721'
        case 116:
          question = 'В каком году произошло провозглашение России империей?'
          correct_answer = '1721'
        case 117:
          question = 'В каком году был издан Табель о рангах?'
          correct_answer = '1722'
        case 118:
          question = 'В каком году был издан Указ о престолонаследии Петра I?'
          correct_answer = '1722'
        case 119:
          question = 'В каком году произошло открытие Академии наук в Санкт-Петербурге?'
          correct_answer = '1725'
        case 120:
          question = 'В каком году произошло создание Верховного тайного совета?'
          correct_answer = '1726'
        case 121:
            question = 'В каком году произошла ссылка Меншикова в Березов?'
            correct_answer = '1727'
        case 122:
            question = 'В каком году произошла отмена указа о единонаследии?'
            correct_answer = '1731'
        case 123:
            question = 'В каком году произошло открытие Сухопутного шляхетского (кадетского) корпуса?'
            correct_answer = '1732'
        case 124:
            question = 'В каком году был подписан Рештский договор с Персией?'
            correct_answer = '1732'
        case 125:
            question = 'В каком году был подписан Белградский мир с Турцией?'
            correct_answer = '1739'
        case 126:
            question = 'В каком году произошло свержение Ивана VI?'
            correct_answer = '1741'
        case 127:
            question = 'В каком году был подписан Абосский мир с Швецией?'
            correct_answer = '1743'
        case 128:
            question = 'В каком году произошла Отмена внутренних таможенных пошлин?'
            correct_answer = '1754'
        case 129:
            question = 'В каком году произошло открытие Московского университета?'
            correct_answer = '1755'
        case 130:
            question = 'В каком году произошла битва при Гросс-Егерсдорфе?'
            correct_answer = '1757'
        case 131:
            question = 'В каком году произошло издание Указа о присоединении Восточной Пруссии к России?'
            correct_answer = '1758'
        case 132:
            question = 'В каком году произошла битва при Цорндорфе?'
            correct_answer = '1758'
        case 133:
            question = 'В каком году произошла битва при Кунерсдорфе?'
            correct_answer = '1759'
        case 134:
            question = 'В каком году произошло взятие Берлина в Семилетнюю войну?'
            correct_answer = '1760'
        case 135:
            question = 'В каком году произошло подписание Петербургский мир после Семилетней войны?'
            correct_answer = '1762'
        case 136:
            question = 'В каком году произошло издание Манифеста о вольности дворянской?'
            correct_answer = '1762'
        case 137:
            question = 'В каком году произошла Секулиризация церковных земель?'
            correct_answer = '1764'
        case 138:
            question = 'В каком году произошел Созыв Уложенной комиссии?'
            correct_answer = '1767'
        case 139:
            question = 'В каком году произошел роспуск Уложенной комиссии?'
            correct_answer = '1768'
        case 140:
            question = 'В каком году начался выпуск ассигнаций?'
            correct_answer = '1768'
        case 141:
            question = 'В каком году произошли битвы у реки Ларги и у реки Кагул?'
            correct_answer = '1770'
        case 142:
            question = 'В каком году произошло Чесменское сражение?'
            correct_answer = '1770'
        case 143:
            question = 'В каком году произошел Первый раздел Речи Посполитой?'
            correct_answer = '1772'
        case 144:
            question = 'В каком году произошло подписание мира в Кючук-Кайнарджи?'
            correct_answer = '1774'
        case 145:
            question = 'В каком году была проведена Губернская реформа Екатерины II?'
            correct_answer = '1775'
        case 146:
            question = 'В каком году произошло присоединение Крыма к России Екатериной II?'
            correct_answer = '1783'
        case 147:
            question = 'В каком году произошло издание Жалованной грамоты дворянству и Жалованной грамоты городам?'
            correct_answer = '1785'
        case 148:
            question = 'В каком году была оборона крепости Кинбурн Суворовым?'
            correct_answer = '1787'
        case 149:
            question = 'В каком году произошло взятие Очакова войсками Потемкина?'
            correct_answer = '1788'
        case 150:
            question = 'В каком году произошли битвы при Фокшанах и Рымнике?'
            correct_answer = '1789'
        case 151:
            question = 'В каком году произошло взятие Измаила Суворовым?'
            correct_answer = '1790'
        case 152:
            question = 'В каком году произошел бой у мыса Калиакрия?'
            correct_answer = '1791'
        case 153:
            question = 'В каком году произошли Второй раздел Речи Посполитой и восстание Костюшко?'
            correct_answer = '1793'
        case 154:
            question = 'В каком году был заключен Ясский мирный договор?'
            correct_answer = '1791'
        case 155:
            question = 'В каком году произошел Третий раздел Речи Посполитой?'
            correct_answer = '1795'
        case 156:
            question = 'В каком году произошло подписание Манифеста о трехдневной барщине?'
            correct_answer = '1797'
        case 157:
            question = 'В каком году был подписан Указ о престолонаследии Павла I?'
            correct_answer = '1797'
        case 158:
            question = 'В каком году произошло освобождение острова Корфу от французской окупации?'
            correct_answer = '1799'
        case 159:
            question = 'В каком году произошли Итальянский и Швейцарский походы Суворова?'
            correct_answer = '1799'
        case 160:
            question = 'В каком году произошел переход Суворова через Альпы?'
            correct_answer = '1799'
        case 161:
            question = 'В каком году произошло убийство Павла I заговорщиками ?'
            correct_answer = '1801'
        case 162:
            question = 'В каком году были созданы первые министерства?'
            correct_answer = '1802'
        case 163:
            question = 'В каком году был принят Указ о Вольных хлебопашцах?'
            correct_answer = '1803'
        case 164:
            question = 'В каком году был издан университетского устава Алексндра I?'
            correct_answer = '1804'
        case 165:
            question = 'В каком году произошла битва при Аустерлице?'
            correct_answer = '1805'
        case 166:
            question = 'В каком году произошло сражение при Прейсиш-Эйлау?'
            correct_answer = '1807'
        case 167:
            question = 'В каком году произошло сражение под Фридландом?'
            correct_answer = '1807'
        case 168:
            question = 'В каком году был подписан Тильзитский мир?'
            correct_answer = '1807'
        case 169:
            question = 'В каком году был подписан Фридрихсгамский мирный договор?'
            correct_answer = '1809'
        case 170:
            question = 'В каком году произошло создание Государственного Совета?'
            correct_answer = '1810'
        case 171:
            question = 'В каком году произошло создание Царскосельского лицея?'
            correct_answer = '1811'
        case 172:
            question = 'В каком году был подписан Бухарестский мир с Турцией?'
            correct_answer = '1812'
        case 173:
            question = 'В каком месяце 1812 года произошло Смоленское сражение? Ответ запишите числом.'
            correct_answer = '8'
        case 174:
            question = 'В каком месяце 1812 года произошла Бородинская битва? Ответ запишите числом.'
            correct_answer = '8'
        case 175:
            question = 'В каком месяце 1812 года произошел Совет в Филях? Ответ запишите числом'
            correct_answer = '9'
        case 176:
            question = 'В каком месяце 1812 года произошел Тарутинский маневр? Ответ запишите числом'
            correct_answer = '9'
        case 177:
            question = 'В каком месяце 1812 года произошел бой под Малоярославцем? Ответ запишите числом'
            correct_answer = '10'
        case 178:
            question = 'В каком месяце 1812 года произошло сражение у города Красный? Ответ запишите числом'
            correct_answer = '11'
        case 179:
            question = 'В каком месяце 1812 года произошла переправа французских войск через Березину? Ответ запишите числом.'
            correct_answer = '11'
        case 180:
            question = 'В каком месяце 1812 года произошло издание Манифеста об окончании войны? Ответ запишите числом.'
            correct_answer = '12'
        case 181:
            question = 'В каком году был подписан Гюлистанский мир с Персией?'
            correct_answer = '1814'
        case 182:
            question = 'В каком году произошла «Битва народов» при Лейпциге?'
            correct_answer = '1813'
        case 183:
            question = 'В каком году был заключен Парижский мир после наполеоновских войн?'
            correct_answer = '1814'
        case 184:
            question = 'В каком году произошло событие, известное как «Сто дней Наполеона»?'
            correct_answer = '1815'
        case 185:
            question = 'В каком году произошло дарование конституции Царству Польскому?'
            correct_answer = '1815'
        case 186:
            question = 'В каком году произошло cоздание Союза Спасения?'
            correct_answer = '1816'
        case 187:
            question = 'В каком году произошло ?'
            correct_answer = ''
        case 188:
            question = 'В каком году произошло cоздание Союза Благоденствия?'
            correct_answer = '1818'
        case 189:
            question = 'В каком году произошло Восстание декабристов?'
            correct_answer = '1825'
        case 190:
            question = 'В каком году произошло cоздание Собственной Его Императорского Величества Канцелярии ?'
            correct_answer = '1826'
        case 191:
            question = 'В каком году был издан "Чугунный" цензурный устав?'
            correct_answer = '1826'
        case 192:
            question = 'В каком году был подписан Туркманчайский мирный договор?'
            correct_answer = '1828'
        case 193:
            question = 'В каком году произошло Наваринское морское сражение?'
            correct_answer = '1827'
        case 194:
            question = 'В каком году был заключен Адрионопольский мирный договор?'
            correct_answer = '1829'
        case 195:
            question = 'В каком году произошло утверждение положения о почетных гражданах?'
            correct_answer = '1832'
        case 196:
            question = 'В каком году произошло окончание кодификации законов в Российской империи?'
            correct_answer = '1832'






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



