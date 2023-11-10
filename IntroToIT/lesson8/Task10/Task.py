#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    """
    Функция для нахождения второго наибольшего числа в списке
    :param numbers: список, второй наибольший элемент которого нужно найти
    :return second: второе наибольшее число списка
    :Note : Функция вернет None, если в списке не окажется второго наибольшего
            числа
    """
    first = second = float('-inf')
    for n in numbers:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n
    return second if second != float('-inf') else None
print(second_largest([10, 4, 9, 4, 9, 10, 4]))  # Должно вывести 9
