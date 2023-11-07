#INTRO TO IT 2nd COURSE
#Отредактировать код так, что бы он соответствовал кодстайлу

# Функция для вычисления суммы двух чисел
def add(num1, num2):
    return num1 + num2


# Функция для вычисления разности двух чисел
def subtract(num1, num2):
    return num1 - num2

# Функция для вычисления произведения двух чисел
def multiply(num1, num2):
    return num1 * num2

# Функция для вычисления частного двух чисел
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Деление на ноль невозможно"
    
# Ввод двух чисел от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
# Выполняем операции с числами и выводим результаты
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")