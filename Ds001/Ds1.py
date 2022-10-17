# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

try:
    num1 = float(input('Введите число: '))
    num2 = num1
    if num1 < 0:
        num1 = num1 * -1
    count = 0

    while num2 % 1 > 0:
        num2 *= 10
        count += 1
    count += 1
    multiplier = 10 ** count
    num1 = num1 * multiplier

    suma = 0
    while num1 > 0:
        suma = suma + num1 % 10
        num1 = num1 // 10
        
    print (f'Сумма цифр в числе = {int(suma)}')
except: print ('!! Введите число !!')