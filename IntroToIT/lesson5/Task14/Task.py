#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка.
# Неправильное решение:
def wrong_sum_of_two_largest(lst):
    lst_temp = lst.copy()
    first_max = max(lst_temp)
    lst_temp.remove(first_max)
    second_max = max(lst_temp)
    return first_max + second_max

