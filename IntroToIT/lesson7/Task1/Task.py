#INTRO TO IT 2nd COURSE
def add_numbers(a, b):
    # складывает два числа и возвращает их сумму
    result = a + b
    return result

def multiply_numbers(a, b):
    # перемножает два числа и возвращает их произведение
    result = a * b
    return result

def find_max_number(numbers):
    # находит максимально число из итератора и возвращает его
    max_number = max(numbers)
    return max_number

def calculate_factorial(n):
    # вычисляет факториал числа (n!)
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def is_even(number):
    # проверяет, является число четным, если это так, то возвращает True, иначе False
    if number % 2 == 0:
        return True
    else:
        return False


# инициализируем два числа, список чисел и создаем переменные, куда присваиваем значения функций, в которые мы передали эти же переменные
num1 = 10
num2 = 5
sum_result = add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
numbers_list = [3, 8, 1, 6, 12]
max_num = find_max_number(numbers_list)
factorial_result = calculate_factorial(5)
is_even_num = is_even(7)

# выводим вместе с пояснением значения функций
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")