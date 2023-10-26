#INTRO TO IT 2nd COURSE

# Задача 15: Подсчитать количество четных чисел в списке.
# Правильное решение:
def correct_count_even(lst):
    print(len([x for x in lst if x % 2 == 0]))
    return len([x for x in lst if x % 2 == 0])

# not(Неправильное) решение:
def correct2_count_even(lst):
    c = 0
    for num in lst:
        if not num % 2:
            c += 1
        else:
            c == c
    print(c)
    return c
correct_count_even([2, 3, 1, 6, 8, 0, 4])
correct2_count_even([2, 3, 1, 6, 8, 0, 4])