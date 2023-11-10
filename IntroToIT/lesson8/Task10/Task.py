#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    '''
    Функция для нахождения второго наибольшего число в списке
    :param numbers: Список
    :return: Число
    '''

    maxx = max(numbers) # Находим максимальное число из списка
    for i in numbers:
        if maxx == i:
            numbers.remove(i)   # Удаляем из списка все числа, \
                                # равные максимальному
    return max(numbers)

print(second_largest([10, 4, 9, 4, 9, 10, 4]))
