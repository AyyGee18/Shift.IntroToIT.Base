#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def wrong_sum_of_two_largest(lst):
    return sorted(lst)[-1] + sorted(lst)[-2]
