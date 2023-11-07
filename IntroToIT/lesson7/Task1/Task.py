#INTRO TO IT 2nd COURSE
def add_numbers(a, b):
    '''Функция сложения числе
    param a: первое число
    param b: Второе число
    '''
    result = a + b
    return result

def multiply_numbers(a, b):
    '''Функция умножение чисел
    param a: 1 число
    param b: 2 число
    '''
    result = a * b
    return result

def find_max_number(numbers):
    '''Функция обнаружения наибольшего числа из списка
    param number: список
    param max_number: наибольшее число
    '''
    max_number = max(numbers)
    return max_number

def calculate_factorial(n):
    '''Функция факториала
    param n: вводимое число
    param factorial: результат факториала
    '''
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def is_even(number):
    '''Функция проверки на чётность
    param number: вводимое число
    '''
    if number % 2 == 0:
        return True
    else:
        return False

num1 = 10
num2 = 5
#Сложение чисел
sum_result = add_numbers(num1, num2)
#Умножение чисел
product_result = multiply_numbers(num1, num2)
numbers_list = [3, 8, 1, 6, 12]
#Поиск максимального значения
max_num = find_max_number(numbers_list)
#Факториал
factorial_result = calculate_factorial(5)
#Проверка на чётность
is_even_num = is_even(7)
#Выводы результатов
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")
