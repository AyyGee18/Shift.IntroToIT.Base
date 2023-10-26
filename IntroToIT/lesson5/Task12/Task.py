#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Неправильное решение:
def correct_unique_elements(lst):
    new_lst = []
    for item in lst:
        if item in new_lst:
            new_lst.remove(item)
            new_lst.append(item)
        else:
            new_lst.append(item)
    print(new_lst)
    return new_lst
correct_unique_elements([3, 2, 2, 0, 4, 8, 0, 33, 2])