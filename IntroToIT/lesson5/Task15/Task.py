#INTRO TO IT 2nd COURSE

# Задача 15: Подсчитать количество четных чисел в списке.
# Правильное решение(Оно тут уже было):
def correct_count_even(lst):
    return len([x for x in lst if x % 2 == 0])
