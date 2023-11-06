#INTRO TO IT 2nd COURSE
def add_numbers(a, b):
    """
    Функция для сложения двух числе.
    :param a: Первое число.
    :param b: Второе число.
    :return: Сумма чисел.
    """
    result = a + b
    return result

def multiply_numbers(a, b):
    """
    Функция для перемножения двух числе.
    :param a: Первое число.
    :param b: Второе число.
    :return: Перемноженные 2 числа.
    """
    result = a * b
    return result

def find_max_number(numbers):
    """
    Функция для нахождения максимального числа из списка.
    :param numbers: Список, в котором мы ищем максимальное число.
    :return: Максимальное число списка.
    """
    max_number = max(numbers)
    return max_number

def calculate_factorial(n):
    """
    Функция для нахождения факториала числа.
    :param n: Число, которого факториал мы ищем.
    :return: Факториал заданного числа.
    """
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def is_even(number):
    """
    Функция для проверки чпетности числа.
    :param number: Число для проверки.
    :return: Истенна ли проверка.
    """
    if number % 2 == 0:
        return True
    else:
        return False

num1 = 10
num2 = 5
sum_result = add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
numbers_list = [3, 8, 1, 6, 12]
max_num = find_max_number(numbers_list)
factorial_result = calculate_factorial(5)
is_even_num = is_even(7)

print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")