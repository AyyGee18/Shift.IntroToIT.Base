#INTRO TO IT 2nd COURSE
# sum of two numbers
def add_numbers(a, b):
    '''
    param a: first num
    param b: second num
    return: sum of nums
    '''
    result = a + b
    return result
# multiplication of numbers
def multiply_numbers(a, b):
    '''
    param a: first num
    param b: second num
    return: multiplication of nums
    '''
    result = a * b
    return result
# max in arr
def find_max_number(numbers):
    '''
    param numbers: arr of nums
    return: max in arr
    '''
    max_number = max(numbers)
    return max_number
# factorial of number
def calculate_factorial(n):
    '''
    param n: num
    return: factorial
    '''
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial
# check of eventity
def is_even(number):
    '''
    param number: num
    return: is_even
    '''
    if number % 2 == 0:
        return True
    else:
        return False

# some nums
num1 = 10

num2 = 5
#func calls
sum_result = add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
# some arr
numbers_list = [3, 8, 1, 6, 12]
#func calls
max_num = find_max_number(numbers_list)
factorial_result = calculate_factorial(5)
is_even_num = is_even(7)

# out
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")