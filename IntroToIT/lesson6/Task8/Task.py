#INTRO TO IT 2nd COURSE
#Задача 8: Подсчет суммы цифр в числе
def sum_of_digits(number):
    n=number
    s=0
    while (n!=0):
        s+=n%10
        n//=10
    return s