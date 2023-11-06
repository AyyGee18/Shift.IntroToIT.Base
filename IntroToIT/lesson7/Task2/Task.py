#INTRO TO IT 2nd COURSE
#Отредактировать код так, что бы он соответствовал кодстайлу

# Функция для вычисления суммы двух чисел
def add_numbers(a, b):
    return a + b
# Функция для вычисления разности двух чисел
def subtract_numbers(a, b):
    return a - b
# Функция для вычисления произведения двух чисел
def multiply_numbers(a, b):
    return a * b
# Функция для вычисления частного двух чисел
def division_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Деление на ноль невозможно"
    
# Ввод двух чисел от пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Выполняем операции с числами и выводим результаты
print(f"{ num1 } + { num2 } = { add_numbers(num1, num2) }")
print(f"{ num1 } - { num2 } = { subtract_numbers(num1, num2) }")
print(f"{ num1 } * { num2 } = { multiply_numbers(num1, num2) }")
print(f"{ num1 } / { num2 } = { division_numbers(num1, num2) }")