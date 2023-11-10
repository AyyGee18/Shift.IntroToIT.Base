#INTRO TO IT 2nd COURSE
# Задача: вернуть строку в обратном порядке
def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = s[::-1]  # неправильное присваивание для реверсирования строки
    return reversed_s
