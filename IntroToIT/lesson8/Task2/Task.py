#INTRO TO IT 2nd COURSE
# Задача: найти минимальное число в списке
def find_min(lst):
    if not lst:
        return None
    min_num = lst[0]
    for num in lst[1:]:
        if num < min_num:  
            min_num = num #если текущий элемент меньше min_num, обновляем минимальный элемент
    return min_num