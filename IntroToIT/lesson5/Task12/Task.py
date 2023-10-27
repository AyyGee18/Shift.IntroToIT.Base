#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Правильное решение :)
def not_wrong_unique_elements(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst