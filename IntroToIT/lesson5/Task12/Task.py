#INTRO TO IT 2nd COURSE
# Задача 12: Вернуть список без дубликатов. 
# Правильное решение:

lst = ['cat', 'dog', 'cat', 'cat', 'dog', 'hen']

def unique_elements(lst):
    new_lst = []
    for item in lst:
        if item  not in new_lst:
            new_lst.append(item)

    print(new_lst)

unique_elements(lst)