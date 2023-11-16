#INTRO TO IT 2nd COURSE
# Задача: вывести числа от 1 до N, пропуская числа, которые делятся на M
def print_numbers_skip_divisible(n, m):
    for i in range(1, n+1):
        p = []
        if i % m != 0:
            p+=[i]
        print(p)

print_numbers_skip_divisible(16, 8)