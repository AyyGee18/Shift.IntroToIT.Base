#INTRO TO IT 2nd COURSE
# Задача: проверить, является ли число простым
def is_prime(num):
    if num <= 1:
        print('False')
        return False
    for i in range(2, num):
        if num % i == 0:
            print('False')
            return False
    print('True')
    return True
is_prime(13)
