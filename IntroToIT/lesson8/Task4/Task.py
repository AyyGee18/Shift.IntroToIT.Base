#INTRO TO IT 2nd COURSE
# Задача: проверить, является ли число простым
from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num))+1):  # верхняя граница в цикле не правильная
        if num % i == 0:
            return False
    return True
