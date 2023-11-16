#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    first = [max(numbers)]
    second = float('-inf')
    while any(element in first for element in numbers):
        numbers.remove(max(numbers))
    second = max(numbers)
    return second if second != float('-inf') else None

print(second_largest([10, 4, 9, 4, 9, 10, 4]))  # Должно вывести 9