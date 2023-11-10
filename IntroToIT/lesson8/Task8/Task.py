#INTRO TO IT 2nd COURSE
# Задача: вывести числа от 1 до N, пропуская числа, которые делятся на M
def print_numbers_skip_divisible(n, m):
    '''
    Функция для вывода чисел от 1 до N, пропуская числа, \
        которые делятся на M
    :param n: Число - граница списка
    :param m: Исключаемый делитель
    :return: Вывод подходящих чисел
    '''
    for i in range(1, n+1):
        if i % m == 0:
            pass
        print(i) 
