#INTRO TO IT 2nd COURSE

# Задача 14: Сумма двух наибольших элементов списка. 

lst_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Правильное решение:
def sum_of_two_largest(lst):
   lst.sort()
   print(lst[-1] + lst[-2])

sum_of_two_largest(lst_2)