#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
def sum_of_two_largest(lst):
    first_max = max(lst)
    lst.remove(first_max)
    second_max = max(lst)
    return first_max + second_max

lst = [1,5,10,4,13]
print(sum_of_two_largest(lst))

