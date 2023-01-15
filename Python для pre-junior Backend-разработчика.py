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

# n = int(input())
# p = []
#
# for i in range(n):
#     row = [1] * (i+1)
#     for j in range(i+1):
#         if j != 0 and j != i:
#             row[j] = p[i-1][j-1] + p[i-1][j]
#     p.append(row)
#
# for r in p:
#     print(*r, sep='')


# num = int(input())
# def convert_base(num, to_base=5, from_base=10):
#     # first convert to decimal number
#     if isinstance(num, str):
#         n = int(num, from_base)
#     else:
#         n = int(num)
#     # now convert decimal to 'to_base' base
#     alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if n < to_base:
#         return alphabet[n]
#     else:
#         return convert_base(n // to_base, to_base) + alphabet[n % to_base]
#
# print(convert_base(num))


# n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# flag = True
# def convert_base(num, to_base=2, from_base=10):
#     # first convert to decimal number
#     if isinstance(num, str):
#         n = int(num, from_base)
#     else:
#         n = int(num)
#     # now convert decimal to 'to_base' base
#     alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     if n < to_base:
#         return alphabet[n]
#     else:
#         return convert_base(n // to_base, to_base) + alphabet[n % to_base]
#
# res = convert_base(n1) + convert_base(n2) + convert_base(n3) + convert_base(n4)
# for i in range(len(res)-1):
#     if res[i] == '0' and res[i+1] == '1':
#         flag = False
#         break
# print(flag)

# s = input()
# step = int(input())
# for i in s:
#     if i == 'x':
#         print('a',end='')
#     elif i == 'y':
#         print('b',end='')
#     elif i == 'z':
#         print('c',end='')
#     else:
#         print(chr(ord(i)+step),end='')
#
# print(ord('x'))
# print(ord('y'))
# print(ord('z'))
# print(ord('a'))
#
#
# import operator
# from functools import reduce
#
# print(reduce(operator.mul, [int(i) for i in input().split()]))
#
# from functools import reduce
# print(reduce(lambda x, y: int(x) * int(y), input().split()))
#
# print(eval('*'.join(input().split())))
#
#
# a = {int(i) for i in input().split()}
# res = list(a)
# res.sort()
# print(res[-2])
#
# print(sorted(set(map(int, input().split())))[-2])


# a = [int(i) for i in input().split()]
# for i in range(len(a)):
#     a.remove(0)
#     a.append(0)
# print(*a)
#
# a = [int(i) for i in input().split()]
# new = sorted(a, key=lambda n: n != 0, reverse=True)
# print(*new)
#
#
# print(*sorted(map(int, input().split()),key=lambda x: x==0))
#
# print(*[int(i) for i in input().split() if i % 2 == 0])
#
# print(*filter(lambda x: x % 2 == 0, map(int, input().split())))

# import math
#
# a = sorted([6, 2, 3])
# l = len(a) + 1
# l2 = 0
# if (l + 1) % 2 == 0:
#     l = len(a) // 2 - 1
#     l2 = len(a) // 2 + 1
#     print(int((a[l] + a[l2]) / 2))
# else:
#     l = math.floor(l / 2)
#     print(a[l])


# commands = ['git push origin main']
#
# for command in commands:
#     match command.split():
#         case 'git', 'add', path:
#             print(f'В индекс добавлены файлы по пути: {path}.')
#         case 'git', 'commit':
#             print('Файлы закоммичены.')
#         case 'git', 'commit', '-m', message:
#             print(f'Файлы закоммичены с сообщением {message}')
#         case 'git', 'push', repository, branch:
#             print(f'Файлы запушены в {repository} в ветку {branch}.')
#         case _:
#             print('Неизвестная команда.')


# a = set()
# while i := int(input()):
#     a.add(i)
# print(len(a)+1)

# print(
#     len(
#         {
#             i.replace('b','d',1) if i.startswith('b') else i.replace('c','')
#             for i in ['aa','bbb','cccc', 'bacbac'] if len(i) > 2
#         }
#     )
# )


# a,b,c = [set(input().split()) for i in range(3)]
# print(c - b == a)
#
#
# s = input().split()
# a = {i: s.count(i) for i in s}
# sort = sorted(a.items(), key=lambda x: x[0])
# a = dict(sort)
# for key,values in a.items():
#     print(key,values)
#
# s = input().split()
# d = {}
# for i in s:
#     if i not in d:
#         d[i] = 0
#     d[i] += 1
# for key, value in sorted(d.items()):
#     print(key, value)


# import json
# answer = 0
# d = json.loads(input())
# for i in range(len(d)):
#     if d[i]['age'] > answer:
#         answer = d[i]['age']
#         if d[i]['chief']['age'] > answer:
#             answer = d[i]['chief']['age']
# print(answer)


# print({i if i == 24 else 'ff': i*i for i in [j for j in range(100)] if i % 17 == 0}['ff'])
#
# catalog = []
# while (n := int(input())) != -1:
#     catalog.append(n)
#
# for i in catalog[::-1]:
#     print(i)


# command = input().split()
# stek = []
# while command[0] != 'close':
#     if command[0] == 'add':
#         stek.append(command[int(1)])
#     if command[0] == 'pop':
#         print(stek.pop())
#     if command[0] == 'head':
#         print(stek[-1])
#     command = input().split()
#
#
#
# while (command := input()) != "close":
#     match command.split():
#         case "add", n:
#             stack.append(n)
#         case "pop",:
#             print(stack.pop())
#         case "head",:
#             print(stack[-1])

