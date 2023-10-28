#INTRO TO IT 2nd COURSE
# Задача 9: Переворот строки
def reverse_string(s):
    s2 = sorted(s, reverse=True)
    new = ''.join(s2)
    return new