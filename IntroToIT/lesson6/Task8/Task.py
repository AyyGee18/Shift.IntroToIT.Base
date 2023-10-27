#INTRO TO IT 2nd COURSE
#Задача 8: Подсчет суммы цифр в числе
def sum_of_digits(number):
    s = 0
    for i in str(number):
        s += int(i)
    return s