#INTRO TO IT 2nd COURSE
# Задача: вычислить факториал числа
def factorial(n):
    
    """
    Функция для нахождения факториала числа
    :param n: число, факториал которого нужно найти
    :return result: факториал числа n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
