# word = input()
# print('YES' if word == word[::-1] else 'NO')

# s = 'efgabcd'
# print(s[(len(s) + 1) // 2:] + s[:(len(s)+1) // 2])
# print(s[-(len(s)//-2):]+s[:-(len(s)//-2)])

# print('YES' if (s := input()) == s.title() else 'NO')
#
# print('YES' if 'хорош' in input().lower() else 'NO')
#
# print(sum(s.islower() for s in input()))
#
# n = int(input())
# count = 0
# while n > 0:
#     s = input()
#     if s.count('11') >= 3:
#         count += 1
#     n -= 1
# print(count)
#
# print(sum(input().count('11') > 2 for _ in range(int(input()))))
#
# n = input()
# count = 0
# for i in range(10):
#     count += n.count(str(i))
# print(count)
#
# s = input()
# print('YES' if s.endswith('.com') or s.endswith('.ru') else 'NO')
#
# s = 'aaaaabbbbbccc'
# dictionary = {symbol: s.count(symbol) for symbol in s}
# print(dictionary[max(dictionary, key=dictionary.get)])
# print(max(dictionary, key=dictionary.get))


# s = 'aaaaabbbbbccc'
# a = 0
# fin = ''
# for i in range(len(s)):
#     if s.count(s[i]) >= a:
#         fin = s[i]
# print(fin)
#
# s = 'aaaaabbbbbccc'
# max = 0
# b = 0
# for i in s:
#     if s.count(i) >= max:
#         max = s.count(i)
#         b = i
# print(b)

# a = input()[::-1]
# z = max(a, key = a.count)
# print(z)
#
#
# s = input()
# if s.count('f') > 1:
#     print(s.find('f'),s.rfind('f'))
# elif s.count('f') == 1:
#     print(s.find('f'))
# else:
#     print('NO')
#
# text = input()
# print(text[:text.find("h")] + text[text.rfind("h") + 1:])
#
# print(*[chr(i) for i in range(int(input()), int(input())+1)])
#
# cod = int(input())
# s = input()
# for i in s:
#     dec = ord(i)-cod
#     if dec < 97:
#         dec += 26
#     print(chr(dec), end='')
#
#
# n = int(input())
# s = input()
# res = ''
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(len(s)):
#     res += alphabet[alphabet.find(s[i])-n]
# print(res)


# from string import ascii_lowercase
#
# tot = []
# for i in range(1, 27):
#     tot.append(i * ascii_lowercase[i - 1])
#
# print(tot)
#
# n = int(input())
# catalog = []
# for i in range(n):
#     catalog.append(int(input()))
#
# print(*catalog, sep='\n')
# print()
# for i in catalog:
#     print(i ** 2 + i * 2 + 1)
#
# numbers = [int(input()) for _ in range(int(input()))]
# print(*numbers, '',*[(x + 1) ** 2 for x in numbers], sep='\n')
#
#
#
# n = int(input())
# catalog = []
# for i in range(n):
#     catalog.append(int(input()))
# catalog.remove(max(catalog))
# catalog.remove(min(catalog))
# print(*catalog, sep='\n')
#
#
# ls = [int(input()) for _ in range(int(input()))]
# [print(i) for i in ls if i not in (max(ls), min(ls))]
#
#
# a = [int(input()) for i in range(int(input()))]
# for i in a:
#     if  min(a) < i < max(a):
#         print(i)
#
#
# catalog = [input() for i in range(int(input()))]
# list = []
# for i in catalog:
#     if i not in list:
#         list.append(i)
# print(*list, sep='\n')
#
#
# s = [input() for _ in range(int(input()))]
# print(*[s[i] for i in range(len(s)) if s[:i].count(s[i]) == 0], sep="\n")
#
#
# catalog = [input() for i in range(int(input()))]
# word = input()
# for i in catalog:
#     if word.lower() in i.lower():
#         print(i)
#
# s = [input() for _ in range(int(input()))]
# word = input().lower()
# print(*[i for i in s if word in i.lower()], sep='\n')
#
#
# n = int(input())
# x = [int(input()) for _ in range(n)]
# [print(i) for i in x if i < 0]
# [print(i) for i in x if i == 0]
# [print(i) for i in x if i > 0]
#
# ss = [input() for _ in range(int(input()))]
# reqs = [input().lower() for _ in range(int(input()))]
# print(*[s for s in ss if all(req in s.lower() for req in reqs)], sep='\n')
#
# s = [input() for _ in range(int(input()))]
# search = [input().lower() for i in range(int(input()))]
# st = ''
# for i in search:
#     if i not in st:
#         st += i+' '
# print(*[i for i in s if st in i.lower()], sep='\n')
#
# s = [input() for _ in range(int(input()))]
# d = [input() for _ in range(int(input()))]
# for i in s:
#     for j in d:
#         if j.lower() not in i.lower():
#             break
#     else:
#         print(i)


# s = input().split('.')
# for i in s:
#     if int(i) < 0 or int(i) > 255:
#         print('НЕТ')
#         break
# else:
#     print('ДА')


# s = [int(i) for i in input().split()]
# couple = 0
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if s[i] == s[j]:
#             couple += 1
#
# print(couple)

# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4,5,6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3,25)
# print(numbers)
#
#
# catalog = [int(i) for i in input().split()]
# ma = catalog.index(max(catalog))
# mi = catalog.index(min(catalog))
# if len(catalog) > 1:
#     catalog[mi],catalog[ma] = catalog[ma], catalog[mi]
#
# print(*catalog)
#
#
# s = input().split()
# print(f"Общее количество артиклей: {s.count('a') + s.count('an') + s.count('the')}")
#
#
# n1 = input()
# n = int(n1[1:])
# for i in range(n):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')].rstrip()
#         print(s)
#     else:
#         print(s)
#
#
# n = input()
# for _ in range(int(n[1:])):
#     s = input()
#     if '#' in s:
#         s = s[:s.find('#')]
#     print(s.rstrip())
#
#
# print(*map(lambda i: i.split('#')[0].rstrip(), __import__('sys').stdin.read().splitlines()[1:]), sep='\n')
#
# print(*[input().split('#')[0].rstrip() for i in range(int(input()[1:]))], sep='\n')


# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i[1:] for i in keywords]
#
# print(new_keywords)

#
# palindromes = [i for i in range(100,1001) if i % 10 == i // 100]
#
# print(palindromes)
#

# ---------------------------------------------------Bubble sort------------------------------------------------------
# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
#
# for i in range(n - 1):
#     flag = True
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = False
#             if flag:
#                 break
#
# print(a)


# ------------------------------------Selection sort --------------------------------------------------------------

# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
# sor = []
# n = len(a)
# while len(a) > 0:
#     sor.append(min(a[0:len(a)]))
#     a.remove(min(a))
# print(sor)

# --------------------------------------------------Сортировка простыми вставками-------------------------------------
#
# a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
# n = len(a)
#
# for i in range(1, n):
#     elem = a[i]  # первый элемент из неотсортированной части списка
#     j = i
#     while j >= 1 and a[j - 1] > elem:
#         a[j] = a[j - 1]
#         j -= 1
#     a[j] = elem
#
#
# print('Отсортированный список:', a)


a = [int(i) for i in input().split()]
print(*a,sep='+',end=f'={sum(a)}')