#INTRO TO IT 2nd COURSE
#Рассчитывание дня рождения:
#(Пусть это будет функция, которая возвращает количество дней до дня рождения)
from datetime import datetime
def days_until_birthday(birthday):
    today = datetime.today()
    next_birthday = datetime(today.year, birthday.month, birthday.day)
    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)
    days_until = (next_birthday - today).days
    return days_until

today = datetime(2023, 10, 27)
birthday = datetime(2024, 12, 31)

days = (birthday - today).days
print(f"До вашего дня рождения осталось {days} дней.")