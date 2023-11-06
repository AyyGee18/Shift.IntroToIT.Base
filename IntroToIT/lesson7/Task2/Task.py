#INTRO TO IT 2nd COURSE
#Отредактировать код так, что бы он соответствовал кодстайлу

# Функция для вычисления суммы двух чисел
def sum_digits(a, b):
    return a + b
# Функция для вычисления разности двух чисел
def difference_digits(a, b):
    return a - b
# Функция для вычисления произведения двух чисел
def multiplying_digits(a, b):
    return a * b
# Функция для вычисления частного двух чисел
def quotient_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Деление на ноль невозможно"
# Ввод двух чисел от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
# Выполняем операции с числами и выводим результаты
print(f"{num1} + {num2} = { num1 + num2}")
print(f"{num1} - {num2} = { num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = { num1 / num2}")