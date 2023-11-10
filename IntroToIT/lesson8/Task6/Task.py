#INTRO TO IT 2nd COURSE
# Задача: вернуть строку в обратном порядке
def reverse_string(s):
    reversed_s = ''
    for char in s[::-1]:
        reversed_s += char 
    return reversed_s


