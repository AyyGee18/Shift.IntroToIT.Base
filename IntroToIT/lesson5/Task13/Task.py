#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Неправильное решение:
def wrong_is_sorted(lst):
    flag = 0
    i = 1
    while i < len(lst):
        if (lst[i] < lst[i - 1]):
            flag = 1
        i += 1

    if (not flag):
        print(True)
    else:
        print(False)