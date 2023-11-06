#INTRO TO IT 2nd COURSE
# Сложение полученных чисел
def add_numbers(a, b):
    '''
    a - первое слагаемое
    b - второе слагаемое
    result - сумма a и b
    '''
    result = a + b
    return result
# Произведение двух чисел
def multiply_numbers(a, b):
    '''
    a - первый множитель
    b - второй множитель
    result - произведение a и b
    '''
    result = a * b
    return result
# Нахождение большего числа
def find_max_number(numbers):
    '''
    numbers - список чисел
    max() - функция для нахождения большего числа из списка
    max_number - число полученное после функции max()
    '''
    max_number = max(numbers)
    return max_number
# Факториал числа
def calculate_factorial(n):
    '''
    n - полученное число
    factorial -переменная, которая будет держать значение факториала 'n'.(Изночально в данной переменной записано значение 1)
    Если n = 0, то фозвращается еденица, но если нет, то тогда в цикле for перебирается range от 1 до n + 1 и перемножаются с factorial.
    После этого функция возвращает знечение factorial.
    '''
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
# Чётно или нечётное
def is_even(number):
    '''
    number - полученный аргумент
    Если number делится на два без остатка, то тогда это чётное число, но если оно делится с остатком, то это не чётное число.
    '''
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