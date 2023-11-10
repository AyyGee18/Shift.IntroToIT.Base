#INTRO TO IT 2nd COURSE
# Задача: найти минимальное число в списке
def find_min(lst):
    '''
    Функция для вычисления минимального числа в списке.
    :param lst: Список чисел
    :return: Минимальное число
    '''
    if not lst:
        return None     # Если список пустой, то возвращается None
    min_num = lst[0] 
    for num in lst[1:]:
        if num < min_num:
            min_num = num
    return min_num