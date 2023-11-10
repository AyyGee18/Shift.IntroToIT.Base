#INTRO TO IT 2nd COURSE
# Задача: сгенерировать список всех четных чисел до N
def generate_evens(n):
    return [i for i in range(2, n+1, 2)]  # идём от 2 до заданного числа с шагом = 2
