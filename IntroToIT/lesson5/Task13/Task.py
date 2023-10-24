# INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

# Неправильное решение:

src_lst = [2, 5, 3]


def wrong_is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False


print(wrong_is_sorted(src_lst))
