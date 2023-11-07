#INTRO TO IT 2nd COURSE
#Отредактировать код так, что бы он соответствовал кодстайлу


def add(a: float, b: float) -> float:
    """
    Функция для вычисления суммы двух чисел
    :param a: число a
    :param b: число b
    :return: сумма a и b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Функция для вычисления разности двух чисел
    :param a: число a
    :param b: число b
    :return: разность a и b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Функция для вычисления произведения двух чисел
    :param a: число a
    :param b: число b
    :return: произведение a и b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Функция для вычисления частного двух чисел
    :param a: число a
    :param b: число b
    :return: произведение a и b
    """
    if b != 0:
        return a / b
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