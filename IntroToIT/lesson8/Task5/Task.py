#INTRO TO IT 2nd COURSE
# Задача: сгенерировать список всех четных чисел до N
def generate_evens(n):
    return [i for i in range(2, n) if i % 2 == 0]  # интервал в генераторе списка неправильный