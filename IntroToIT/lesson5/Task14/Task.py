#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def sum_of_two_largest(lst):
    sorted_lst = sorted(lst, reverse=True)
    print(sorted_lst)
    return sorted_lst[0] + sorted_lst[1]
