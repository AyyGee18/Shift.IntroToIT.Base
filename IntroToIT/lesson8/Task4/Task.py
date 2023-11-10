#INTRO TO IT 2nd COURSE
# Задача: проверить, является ли число простым
def is_prime(num):
    '''
    Функция для проверки числа на простоту.
    :param num: Число
    :return: True или False
    '''
    if num <= 1:
        return False
    for i in range(2, num): # Нахождение делителей числа через цикл
        if num % i == 0:
            return False
    return True
