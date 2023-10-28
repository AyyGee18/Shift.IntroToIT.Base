#INTRO TO IT 2nd COURSE

# Задача 15: Подсчитать количество четных чисел в списке.
def count_even(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
        else:
            pass
    return count
lst = [1,2,4,20]
print(count_even(lst))