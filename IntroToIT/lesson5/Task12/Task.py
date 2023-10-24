# INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Неправильное решение:
old_lst = [2, 4, 3, 4, 2, 9]


def wrong_unique_elements(lst):
    return set(lst)


print(wrong_unique_elements(old_lst))
