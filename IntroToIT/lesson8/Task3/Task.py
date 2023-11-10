#INTRO TO IT 2nd COURSE
# Задача: вычислить факториал числа

def factorial(n):
    if n < 0:
        return "Отрицательное число!"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#Работает 

