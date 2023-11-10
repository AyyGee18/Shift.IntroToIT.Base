#INTRO TO IT 2nd COURSE
# Задача: вернуть строку в обратном порядке
def reverse_string(s):
    """
    Функция для 'разворота' строки
    :param s: исходная строка
    :return reversed_s: развернутая строка
    """
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s
