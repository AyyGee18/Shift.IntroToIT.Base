#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Правильное решение:
def is_sorted(lst):
    return lst == sorted(lst)