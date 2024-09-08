# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
import fractions
from fractions import Fraction

numbers = input("введите два числа вида a/b ")
data = numbers.split("/")
summa = int(data[0]) + int(data[1])
composition = int(data[0]) * int(data[1])

print(summa, composition)

print(fractions.Fraction(numerator = int(data[0]), denominator = int(data[1])))





