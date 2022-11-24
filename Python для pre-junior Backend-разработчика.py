# Перевод числа в любую систему исчисление:
# num = int(input())
# base =  int(input('Base (2 - 9): '))
# if not(2 <= base <= 9):
#     quit()
#
# new_num = ''
#
# while num > 0:
#     new_num = str(num % base) + new_num
#     num //= base
# print(new_num)
#
# x = int(input())
# print(x // 8, x % 8, sep='')

# Чему равно минимальное отрицательное число для переменной размером 2 байта?
print(f'-{2**16/2}')