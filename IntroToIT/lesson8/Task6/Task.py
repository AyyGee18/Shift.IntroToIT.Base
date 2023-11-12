#INTRO TO IT 2nd COURSE
# Задача: вернуть строку в обратном порядке
def reverse_string(s):
    reversed_s = ''
    for char in str(s):
        reversed_s += char
        reversed_s1 = reversed_s[::-1]
    print(reversed_s1)
    return reversed_s1
reverse_string(678)