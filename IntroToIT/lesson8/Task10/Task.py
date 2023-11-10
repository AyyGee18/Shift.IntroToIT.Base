#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке
def second_largest(numbers):
    # Предлагаю следующий способ

    if len(numbers) >= 2:
        # Первое наибольшее число
        first = max(numbers)
        # Выкидываем из списка первое наибольшее число
        filtered_numbers = list(filter(lambda x: x != first, numbers))
        # Если список состоял из разных чисел
        if filtered_numbers:
            # Второе наибольшее число
            second = max(filtered_numbers)
            return second
    return None
