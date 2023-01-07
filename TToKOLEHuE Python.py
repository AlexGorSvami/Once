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


s = [int(i) for i in input().split()]
couple = 0
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i] == s[j]:
            couple += 1

print(couple)