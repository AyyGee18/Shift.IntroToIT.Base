#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Неправильное решение:
def is_sorted(lst):
    if sorted(lst) == lst:
        return True
    return False
