#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 
# Неправильное решение:
def wrong_sum_of_two_largest(lst):
    first_max = max(lst)
    lst.remove(first_max)
    second_max = max(lst)
    return first_max + second_max

# Более краткое решение
def wrong_sum_of_two_largest_1(lst):
    lst.sort
    return lst[-1] + lst[-2]

lst = [2,1,3,4,5]
print(wrong_sum_of_two_largest_1(lst))