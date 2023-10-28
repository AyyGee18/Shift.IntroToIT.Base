#INTRO TO IT 2nd COURSE
#Рассчитывание дня рождения:
#(Пусть это будет функция, которая возвращает количество дней до дня рождения)
from datetime import datetime

def days_until_birthday(birZday):
    today = datetime.today()
    next_birthday = datetime(today.year, today.month, today.day)
    if today > next_birthday:
        next_birthday = datetime(today.year, today.month, today.day)
    return (next_birthday - today).days + 1

