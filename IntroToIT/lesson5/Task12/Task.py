#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Правильное решение:
def wrong_unique_elements(lst):
    new_lst = []
    for item in lst:
        if item in new_lst:
            continue
        else:
            new_lst.append(item)
    return new_lst
lst = [1,1,2,3,4,5,5,6,1]
print(wrong_unique_elements(lst))