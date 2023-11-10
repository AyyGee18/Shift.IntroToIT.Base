#INTRO TO IT 2nd COURSE
# Задача: вычислить сумму чисел в списке
def sum_list(lst):
    '''
    Функция для вычисления суммы всех чисел списка.
    :param lst: Список чисел
    :return: Сумма чисел
    '''
    total = 0
    for num in lst:
        total += num
    return total

