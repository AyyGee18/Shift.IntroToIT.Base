#INTRO TO IT 2nd COURSE
def add_numbers(a, b):
    """
    Функция сложения двух чисел.
    :param a: первое число
    :param b: второе число
    :result: сумма чисел 
    """

    result = a + b
    return result


def multiply_numbers(a, b):
    """
    Функция произведения двух чисел.
    :param a: первое число
    :param b: второе число
    :result: произведение чисел 
    """
    result = a * b
    return result


def find_max_number(numbers):
    """
    Функция возвращающая максимальное число.
    :param numbers: все числа
    :param max_number: максимальное число 
    """
    max_number = max(numbers)
    return max_number


def calculate_factorial(n):
    """
    Функция возвращающая факториал числа.
    :param n: число
    Если n == 0, то циклл не отработает 
    """
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def is_even(number):
    """
    Функция проверяющая число на четность.
    :param number: число 
    """
    if number % 2 == 0:
        return True
    else:
        return False

num1 = 10 #первое число
num2 = 5#второе число
sum_result = add_numbers(num1, num2)#вызов функции сложения
product_result = multiply_numbers(num1, num2)#вызов функции умножения
numbers_list = [3, 8, 1, 6, 12]#список чисел
max_num = find_max_number(numbers_list)#вызов функции поиска максимального числа из списка numbers_list
factorial_result = calculate_factorial(5)#вызов функции факториала
is_even_num = is_even(7)# вызов функции проверки четности числа

#вывод всех функций
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")