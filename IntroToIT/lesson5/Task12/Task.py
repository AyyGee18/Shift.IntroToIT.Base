#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
def unique_elements(lst):
    new_lst = []
    for item in lst:
        if item not in new_lst:
          new_lst.append(item)  
    return new_lst
lst = [1,1,2,3,4,4,4,5]
print(unique_elements(lst))