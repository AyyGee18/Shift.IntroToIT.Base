#INTRO TO IT 2nd COURSE
s = str(input("Введите строку: ").replace(' ', '').lower())
if s[::-1]: # s = s[::-1] - опечатка
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
