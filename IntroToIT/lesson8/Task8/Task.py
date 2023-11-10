#INTRO TO IT 2nd COURSE
# Задача: вывести числа от 1 до N, пропуская числа, которые делятся на M
def print_numbers_skip_divisible(n, m):
    if m == 0:
        print('НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!!!')
    else:
        for i in range(1, n+1):
            if not i % m == 0:
                print(i)
                