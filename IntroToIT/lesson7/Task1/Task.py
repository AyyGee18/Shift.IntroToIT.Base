#INTRO TO IT 2nd COURSE

#Эта функция вернет сумму двух чисел
def add_numbers(a, b):
    """
    Функция для сложения двух чисел.
    :param a: Первое число
    :param b: Второе число
    :return result: Сумма чисел
    :Note: На вход должны подаваться обязательно только числа
    """
    result = a + b
    return result

#Эта функция вернет произведение двух чисел
def multiply_numbers(a, b):
    """
    Функция умножения двух чисел.
    :param a: Первое число
    :param b: Второе число
    :return result: Произведение чисел
    :Note: На вход должны обязательно подаваться только числа
    """
    result = a * b
    return result

#Эта функция вернет максимальное число из данного списка или кортежа
def find_max_number(numbers):
    """
    Функция для нахождения наибольшего числа из данного списка или кортежа
    :param numbers: Список или кортеж
    :return result: Наибольшее число из данного списка или кортежа
    """
    max_number = max(numbers)
    return max_number

#Эта функция вернет факториал числа
def calculate_factorial(n):
    """
    Функция для нахождения факториала числа
    :param n: Число, факториал которого нужно найти
    :return  factorial: Факториал данного числа
    :Note: Функция будет работать неправильно при отрицательном n
    """ 
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

#Эта функция проверяет, четное ли число
def is_even(number):
    """
    Функция, которая проверяет, четное ли число
    :param number: Число, которое нужно проверить на четность
    :return: Если число четное - True, иначе - False
    :Note: На вход должны обязательно подаваться только число
    """
    if number % 2 == 0:
        return True
    else:
        return False

#Создание переменных для проверки функций
num1 = 10
num2 = 5
sum_result = add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
numbers_list = [3, 8, 1, 6, 12]
max_num = find_max_number(numbers_list)
factorial_result = calculate_factorial(5)
is_even_num = is_even(7)

#Вызов результата работы функций
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")