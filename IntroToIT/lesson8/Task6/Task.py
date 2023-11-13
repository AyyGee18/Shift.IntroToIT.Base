#INTRO TO IT 2nd COURSE
# Задача: вернуть строку в обратном порядке
def reverse_string(s):
    reversed_s = ''
    for i in range(len(s)-1,-1,-1):
        reversed_s += s[i] # неправильное присваивание для реверсирования строки
    return reversed_s
