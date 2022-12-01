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


# login = input()
# password = input()
# print(len(login) > 4 and len(password) > 8 and login != password)
#
# print(len(login := input()) > 4 and len(password := input()) > 8 and password != login)
# print(len(login := input()) > 4 and len(password := input()) > 8 and password != login)


# password = 'admin'
#
# match password:
#      case 'admin111':
#         print(f'Admin password')
#      case 'user111':
#         print(f'user password')
#      case 'moder111':
#         print(f'Moder password')
#      case _:
#         print(f'password error')
#
# print('Complete')


# role = 'user'
#
# match role:
#     case 'user':
#         print(f'{role}, your level 1')
#     case 'verified':
#         print(f'{role}, your level 2')
#     case 'holder':
#         print(f'{role}, your level 3')
#     case 'creator':
#         print(f'{role}, your level 4')
#     case _:
#         print(f'{role}, nor a role')
#
# print(f'Finish')


# match framework := input():
#     case 'Flask' | 'Django' | 'Fast-API':
#         print(f'Python({framework}),Backend-dev')
#     case 'Angular' | 'React' | 'Vue':
#         print(f'JavaScript/TypeScript({framework}),Frontend-dev')
#     case 'Flutter' | 'React Native':
#         print(f'JavaScript({framework}),Cross-Mobile-dev')
#     case 'Pandas' | 'skit-learn' | 'keras':
#         print(f'Python({framework}),Data-Scientist')
#     case _:
#         print('модель еще не обучена')

# n = int(input())
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)

# n = int(input())
# factorial = 1
#
# for i in range(2, n+1):
#     factorial *=i
#
# print(factorial)

n = int(input())
p = []

for i in range(n):
    row = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            row[j] = p[i-1][j-1] + p[i-1][j]
    p.append(row)

for r in p:
    print(*r, sep='')



