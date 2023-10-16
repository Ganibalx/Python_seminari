"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
📌Преобразуйте его в дату в текущем году.
📌Логируйте ошибки, если текст не соответсвует формату.
"""
import datetime
import logging


format = '{levelname:<5} - {asctime:<20} - {funcName} - {msg}'
logging.basicConfig(filename='my.log.', style='{', filemode='a', encoding='utf-8', level=logging.NOTSET, format=format)
logger = logging.getLogger(__name__)

DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

MOUNTS = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'мая': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12
}

def funk(data):
    try:
        count, days, mount = data.split()
        count = int(count[0])
        days = DAYS.index(days)
        for k, v in MOUNTS.items():
            if mount[:3] in k:
                mount = v
                break
        else:
            logger.error(msg=f'Неверный формат месяца: {data}')
    except ValueError as e:
        logger.error(msg=e)
    start_day = 1
    for i in range(7):
        cur_data = datetime.date(year=datetime.datetime.now().year, month=mount, day=(start_day + i)).weekday()
        if cur_data == days:
            days = (start_day + i) + (7 * (count-1))
    return datetime.date(year=datetime.datetime.now().year, month=mount, day=days)


print(funk('5-й четверг июня'))