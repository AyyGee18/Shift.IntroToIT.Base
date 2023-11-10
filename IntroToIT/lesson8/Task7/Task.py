#INTRO TO IT 2nd COURSE
# Задача: посчитать количество вхождений элемента в список
def count_occurrences(lst, element):
    """
    Функция для нахожения вхождения элемента в список
    :param lst: список, в котором проверяются вхождения элемента
    :param element: элемент, количество вхожений которого нужно найти
    :return count: число вхождений элемента
    """
    count = 0
    for elem in lst:
        if elem == element:
            count += 1
#    return lst.count(element)
    return count
