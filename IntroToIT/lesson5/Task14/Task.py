#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def correct_sum_of_two_largest(lst):
    first_max = max(lst)
    lst.remove(first_max)
    second_max = max(lst)
    print(first_max + second_max)
    return first_max + second_max
correct_sum_of_two_largest([10, 12, 0, 53, 9, 39, 39])