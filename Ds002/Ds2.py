# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

try:
    num = int(input('Введите число: '))
    fact = 1

    print ('[ ', end=' ')
    for i in range(num):
        i = i + 1
        fact = i * fact
        print(fact, end='')
        if i != num:
            print(', ', end=' ')
    print (' ]', end=' ')
except: print ('!! Введите целое число !!')