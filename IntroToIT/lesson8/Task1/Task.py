#INTRO TO IT 2nd COURSE
# Задача: вычислить сумму чисел в списке
def sum_list(lst):
    """
    Функция вычесления суммы чисел списка.
    :lst: Список чисел.
    :return: Сумма чисел.
    """
    total = 0
    for num in lst:
        total += num
        pass # здесь должно быть сложение
    return total
