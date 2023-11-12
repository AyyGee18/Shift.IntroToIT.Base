#INTRO TO IT 2nd COURSE
# Задача: вычислить факториал числа
def factorial(n):
    #k = n
    result = 1
    for i in range(1, n+1):
        result *= i
    print(result)
    return result
factorial(5)
