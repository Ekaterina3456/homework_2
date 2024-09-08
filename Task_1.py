# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

ZERO = 0
HEX = 16

num_orig: int = int(input("введите число "))

res1: str = ""
num = num_orig
while num > 0:
    data = ('a', 'b', 'c', 'd', 'e', 'f')
    res = num % HEX
    num //= HEX
    for key, value in enumerate(data, start = 10):
        if res == key:
            res = value
    res1 = str(res) + res1
# while num > 0:
#     x = num % HEX
#     num //= HEX
#     res = ''
#     if x == 10:
#         res = "a"
#     elif x == 11:
#         res = "b"
#     elif x == 12:
#         res = 'c'
#     elif x == 13:
#         res = 'd'
#     elif x == 14:
#         res = 'e'
#     elif x == 15:
#         res = 'f'
#     else:
#         res = str(x)
#     res1 = res + res1

print(res1)
print(hex(num_orig))

