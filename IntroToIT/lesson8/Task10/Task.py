#INTRO TO IT 2nd COURSE
# Задача: найти второе наибольшее число в списке

def second_largest(numbers):
    first = second = float('-inf')
    numbers.sort()
    if numbers[-2] != numbers[-1]:
        return numbers[-2]
    else:
        return numbers[-3]

#Предупреждение: все сломается нафиг, если и 3 число такое же ;)

print(second_largest([10, 4, 9, 4, 9, 10, 4]))  # Должно вывести 9
