#INTRO TO IT 2nd COURSE
# Задача: вычислить факториал числа
def factorial(n):
    '''
    Функция для вычисления факториала числа.
    :param n: Число
    :return: Факториал числа
    '''
    if n == 1:
        return 1
    return n * factorial(n-1) # Использование рекурсии для нахождения факториала
