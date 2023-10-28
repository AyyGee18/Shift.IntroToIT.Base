#INTRO TO IT 2nd COURSE
#Задача 10: Вычисление факториала
def factorial(n):
    f = 1
    if n == 0:
        return 0
    else:
        while n>1:
            f = f*n
            n -= 1
        return f
        