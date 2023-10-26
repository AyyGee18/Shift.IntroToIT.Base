#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Неправильное решение:
def long_is_sorted(lst):
    k = 0
    b = 0
    for i in range(len(lst) - 1):
        if (lst[i] < lst[i + 1]):
            k+=1
            if k == len(lst)-1 and b ==0:
                print('true')
                return True
            
        elif (lst[i] > lst[i + 1]) and k ==0:
            b +=1
            if b == len(lst)-1:
                print('true')
                return True
        elif k != 0 and b != 0:
            print('false')
            return False
        else:
            print('false')
            return False
        if k != 0 and b != 0:
            print('false')
            return False


long_is_sorted([3, 2, 1, 9])
long_is_sorted([3, 2, 1, 0])
long_is_sorted([1, 2, 3, 4])
long_is_sorted([1, 2, 3, 0])