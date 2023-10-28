#INTRO TO IT 2nd COURSE
#Задача 8: Подсчет суммы цифр в числе
def sum_of_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum