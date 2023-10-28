#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 
def sorted_(lst):
    if sorted(lst) == lst:
        return True
    else:
        return False
lst = [1,2,3,4]
lst1 = [1,3,2,4,2]
print(sorted_(lst))