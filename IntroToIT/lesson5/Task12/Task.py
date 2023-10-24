#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Неправильное решение:
def wrong_unique_elements(lst):
    new_lst = []
    for item in lst:
        if item in new_lst:
            pass
        else:
            new_lst.append(item)
    return new_lst