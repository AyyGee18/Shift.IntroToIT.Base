#INTRO TO IT 2nd COURSE
n = int(input("Введите n: "))
summ = 0
for i in range(1, n+1):
    summ  += i
print("Сумма чисел от 1 до ", n, " равна: ", summ)# +=, пробелы, summ вместо sum,
# чтобы не ругались другие текстовые редакторы для работы с Питоном
