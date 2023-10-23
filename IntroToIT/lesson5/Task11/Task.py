#INTRO TO IT 2nd COURSE
# Задача 11: Вернуть сумму всех элементов списка.
 
lst = [1, 3, 4, 7, 8, 10, 11, 14]

# Правильное решение:
def summ_elements(lst):
    print(sum(lst))


summ_elements(lst)


def true_sum_elements(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]

    print(total)

true_sum_elements(lst)