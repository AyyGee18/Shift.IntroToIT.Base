#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Неправильное решение:
def unique_elements(lst):
    new_lst = []
    for item in lst:
        if item in new_lst:
            new_lst.remove(item)
        if item not in new_lst:
            new_lst.append(item)
    return new_lst

a = [1, 2, 3, 4, 1]
print(unique_elements(a))