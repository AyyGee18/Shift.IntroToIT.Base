#INTRO TO IT 2nd COURSE
# Задача: вернуть строку в обратном порядке
def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s #каждый символ записываем в начало строки reversed_s
    return reversed_s
