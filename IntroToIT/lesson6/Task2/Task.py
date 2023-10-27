#INTRO TO IT 2nd COURSE
#Рассчитывание дня рождения:
#(Пусть это будет функция, которая возвращает количество дней до дня рождения)
from datetime import datetime

def days_until_birthday(birthday):
    today = datetime.today()
    next_birthday = datetime(birthday.year, birthday.month, birthday.day)
    answer = (next_birthday - today).days
    while answer >= 366:
        answer -= 365
    return answer 
