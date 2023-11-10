#INTRO TO IT 2nd COURSE
# Задача: вычислить сумму чисел в списке
def sum_list(lst):
    """
    Функция для нахождения суммы элементов списка
    :param lst: список, сумму чисел которых нужно найти
    :return total: сумма чисел списка
    """

    total = 0
    for num in lst:
        total += num
    return total
