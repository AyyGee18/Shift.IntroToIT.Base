#INTRO TO IT 2nd COURSE
##Отредактировать код так, что бы он соответствовал кодстайлу

# Функция для вычисления суммы двух чисел
def add_num(a, b):
    return a + b

# Функция для вычисления разности двух чисел
def subtract_num(a, b):
    return a - b

# Функция для вычисления произведения двух чисел
def multiply_num(a, b):
    return a * b

# Функция для вычисления частного двух чисел
def divide_num(a, b):
    if b != 0:
        return a / b
    else:
        return "Деление на ноль невозможно"
    
# Ввод двух чисел от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполняем операции с числами и выводим результаты
print(f"{num1} + {num2} = {add_num(num1, num2)}")
print(f"{num1} - {num2} = {subtract_num(num1, num2)}")
print(f"{num1} * {num2} = {multiply_num(num1, num2)}")
print(f"{num1} / {num2} = {divide_num(num1, num2)}")