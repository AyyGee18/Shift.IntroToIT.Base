#INTRO TO IT 2nd COURSE
def add_numbers(a: int, b: int) -> int:
    """
    Функция, складывающая два числа - а и b
    :param a: число a
    :param b: число b
    :return: результат сложения a и b
    """
    result = a + b
    return result

def multiply_numbers(a: int, b: int) -> int:
    """
    Функция, умножающая a и b
    :param a: число a
    :param b: число b
    :return: результат умножения a и b
    """
    result = a * b
    return result

def find_max_number(numbers: list[int]) -> int:
    """ 
    Функция, возвращающая наибольший элемент списка чисел
    :param numbers: список с числами, из которого будет взято наибольшее число
    :retrun: максимальное число из списка
    """
    max_number = max(numbers)
    return max_number

def calculate_factorial(n: int) -> int:
    """
    Функция возволяет получить ыакториал заданного числа
    :param n: заданное число, от которого будет браться факториал
    :return: факториал данного числа
    """
    # факториал от 0 всегда 1
    if n == 0:
        return 1
    # в ином случае перемножаем числа в диапазоне [1, n] с шагом 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def is_even(number: int) -> bool:
    """
    Функция позволяет определить чётное число или нет
    :param number: число над которым будет проводиться проверка на чётность
    :return: чётное число или нет
    """
    if number % 2 == 0:
        return True
    else:
        return False

num1: int = 10
num2: int = 5
sum_result: int = add_numbers(num1, num2)
product_result: int = multiply_numbers(num1, num2)
numbers_list: list[int] = [3, 8, 1, 6, 12]
max_num: int = find_max_number(numbers_list)
factorial_result: int = calculate_factorial(5)
is_even_num: bool = is_even(7)

# Выводим информацию о 1-м и 2-м числах
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")

# Выводим, каков же факториал от пятёрки
print(f"Факториал числа 5 равен {factorial_result}")

# Выводим чётное ли число 7
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")