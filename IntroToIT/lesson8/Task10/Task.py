#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    '''
    Сначало находим наибольшее число и записываем в переменную first.
    После этого мы в цикле for удаляем все элементы равные значению first.
    Потом мы возращаем максимальное значение отредактированного списка.
    '''
    first = max(numbers)
    for n in numbers:
        if n == first:
            numbers.remove(first)
    return max(numbers)

print(second_largest([10, 4, 9, 4, 9, 10, 4]))  # Должно вывести 9
