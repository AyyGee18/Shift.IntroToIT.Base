#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

#Правильное решение:
lst = [1,3, 2, 4, 77, 80, 1, 2, 32]
lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_sorted(lst):
    copy_lst = sorted(lst)
    if copy_lst == lst:
        print(True)
    else:
        print(False)

   

is_sorted(lst)
is_sorted(lst_2)
           
    
