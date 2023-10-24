#INTRO TO IT 2nd COURSE

# Задача 15: Подсчитать количество четных чисел в списке.
# Правильное решение:
def correct_count_even(lst):
    return len([x if x % 2 == 0 else 0 for x in lst])
