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
