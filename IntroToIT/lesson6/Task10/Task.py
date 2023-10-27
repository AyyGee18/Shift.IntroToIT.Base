#INTRO TO IT 2nd COURSE
#Задача 10: Вычисление факториала
def factorial(n):
    total = 1
    for num in range(2, n+1):
        total *= num
    return total