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


# На вход вашему серверу пришло время в минутах, которое провел человек на сайте , а также время начала сессии. Вам нужно определить сколько времени было на цифровых часах у человека, когда он закрывал сайт.
# time_mins = int(input())
# start_hours = int(input())
# start_mins = int(input())
# h = (start_hours + (time_mins // 60))%24
# m = start_mins + (time_mins %60)
# if (start_mins + time_mins % 60) >= 60:
#     h += 1
#     m -= 60
# print(h, m)

# print(13 << 2 >> 1)

# print(int(input()) ^ 47) XOR шифрование


# n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
#     print(False)
# elif n1 == 255 and n2 == 255 and n3 == 255 and n4 == 255:
#     print(False)
# elif n1 > 255 or n2 > 255 or n3 > 255 or n4 > 255:
#     print(False)
# else:
#     print(True)
#
#
# n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# if n1 == n2 == n3 == n4 == 0 or n1 == n2 == n3 == n4 == 255:
#     print(False)
# elif 0 <= n1 <= 255 and 0 <= n2 <= 255 and 0 <= n3 <= 255 and 0 <= n4 <= 255:
#     print(True)
# else:
#     print(False)


# n = int(input())
# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[n % 7])


# n = int(input()) % 7
# if n == 0:
#     print('пн')
# elif n == 1:
#     print('вт')
# elif n == 2:
#     print('ср')
# elif n == 3:
#     print('чт')
# elif n == 4:
#     print('пт')
# elif n == 5:
#     print('сб')
# else:
#     print('вс')

