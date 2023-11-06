#INTRO TO IT 2nd COURSE
#Отредактировать код так, что бы он соответствовал кодстайлу

# Функция для вычисления суммы двух чисел
def add(a, b):
    return a + b

# Функция для вычисления разности двух чисел
def subtract(a, b):
    return a - b

# Функция для вычисления произведения двух чисел
def multiply(a, b):
    return a * b

# Функция для вычисления частного двух чисел
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Деление на ноль невозможно"

# Ввод двух чисел от пользователя
num_1 = float (input("Введите первое число: "))
num_2 = float (input("Введите второе число: "))

# Выполняем операции с числами и выводим результаты
print(f"{num_1} + {num_2} = {add(num_1, num_2)}")
print(f"{num_1} - {num_2} = {subtract(num_1, num_2)}")
print(f"{num_1} * {num_2} = {multiply(num_1, num_2)}")
print(f"{num_1} / {num_2} = {divide(num_1, num_2)}")