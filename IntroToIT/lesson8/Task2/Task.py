#INTRO TO IT 2nd COURSE
# Задача: найти минимальное число в списке
def find_min(lst):

    """
    Функция для нахождения наименьшего числа в списке
    :param lst: список, наименьший элемент коготорого нужно найти
    :return min_num: минимальное число в списке
    :Note : если список, поданный на вход будет пуст, то функция вернет None
    """
    if not lst:
        return None
    min_num = lst[0]
    for num in lst[1:]:
        if min_num > num:
            min_num = num
    return min_num
