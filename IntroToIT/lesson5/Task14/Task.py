#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 


def sum_of_two_largest(lst):
    return sum(sorted(lst)[-2:])

a = [1, 2, 3, 4, 100]
print(sum_of_two_largest(a))