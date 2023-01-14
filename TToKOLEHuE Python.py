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


# [print('YES' if all([i.isdigit() for i in n]) and (n[0] == '7' or len(n[0]) == 3) and len(n[-1]) == 4 and len(n[-2]) == 3 else 'NO') for n in [input().split('-')]]
#
#
# a = [int(i) for i in input().split()]
# print(*a,sep='+',end=f'={sum(a)}')


# # объявление функции
# def draw_box():
#     print('*' * 10)
#     for i in range(12):
#             print('*','*',sep='        ')
#     print('*' * 10)
# # основная программа
# draw_box()  # вызов функции


# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(base // 2 + 2):
#         print(i * fill)
#     for i in range(base // 2, 0, -1):
#         print(i * fill)
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)


# def get_factors(num):
#     cat = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             cat.append(i)
#     return cat
#
# def get_factors(num):
#     return [i for i in range(1, int(num / 2) + 1) if num % i == 0] + [num]
#
# print(get_factors(10))
#
#
# def number_of_factors(num):
#     return len([i for i in range(1, num + 1) if num % i == 0])
#

# def find_all(target, symbol):
#     cat = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             cat.append(i)
#     return cat

# def merge(list1, list2):
#     return sorted(list1 + list2)


# def quick_merge(list1, list2):
#     result = []
#
#     p1 = 0
#     p2 = 0
#
#     while p1 < len(list1) and p2 < len(list2):
#         if list1[p1] <= list2[p2]:
#             result.append(list1[p1])
#             p1 += 1
#         else :
#             result.append(list2[p2])
#             p2 += 1
#
#     if p1 < len(list1):
#         result +=(list1[p1:])
#     if p2 < len(list2):
#         result += (list1[p1:])
#
#     return result
#
#
# list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
# list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
# print(quick_merge(list1, list2))


# n = int(input())
# cat = []
# for i in range(n):
#     cat.append([int(i) for i in input().split()])
# def quick_merge(cat):
#     return print(*sorted([i for j in cat  for i in j]))
#
#
# quick_merge(cat)
#
#
# n=int(input())
# def quick_merge(n):
#     return sorted([int(i) for i in range(n) for i in input().split()])
# print(*quick_merge(n))


# объявление функции
# def is_prime(num):
#     count = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         return True
#     else:
#         return False
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))
#
# def is_prime(num):
#     return len([i for i in range(1, num+1) if num % i == 0]) == 2


# def get_next_prime(num):
#     for i in range(num+1,99999):
#         if len([j for j in range(1, i+1) if i % j == 0]) == 2:
#             return i
#
#
# def get_next_prime(num):
#     num += 1
#     for i in range(2, num):
#         if num % i == 0:
#             return get_next_prime(num)
#     return num


# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for c in password:
#         if c.isupper():
#             flag1 = True
#         elif c.islower():
#             flag2 = True
#         elif c.isdigit():
#             flag3 = True
#     return flag1 and flag2 and flag3
#
#
# def is_password_good(password):
#     upp = [i for i in password if i.isupper()]
#     low = [i for i in password if i.islower()]
#     dig = [i for i in password if i.isdigit()]
#     return all([len(password) >= 8, upp, low, dig])
#
#
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     if password.isupper() or password.islower() or password.isalpha() or password.isdigit():
#         return False
#
#     return True


# def is_one_away(word1, word2):
#     count = 1
#     if len(word1) != len(word2):
#         return False
#     else:
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 count += 1
#         if count == len(word1):
#             return True
#         else:
#             return False

# def is_one_away(word1, word2):
#     return len([i for i in word1 if i not in word2]) == 1 and len(word1) == len(word2)
#
# print(is_one_away('bike', 'hike'))
#
# text = 'Standart - smallest, sell Amstrad nats.'
# text1 = text.lower().strip('?!.,').replace(' ', '').replace('-','').replace(',','').replace('.','').replace('?','')
# print(text1)
# print(text1[::-1])
# print(text1 == text1[::-1])
#
#
# def is_palindrome(text):
#     text = [i.lower() for i in text if i not in (',.!?- ')]
#     return text == text[::-1]


def is_valid_password(password):
    res = password.split(':')
    if len(res) < 4:
        return res[0] == res[0][::-1] and int(res[1]) % 2 != 0 and int(res[2]) % 2 == 0
    else:
        return False


def is_valid_password(password):
    password = password.split(':')
    return (password[0] == password[0][::-1]) and (len([i for i in range(1, int(password[1])+1) if int(password[1]) % i == 0]) == 2) and (int(password[2]) % 2 == 0)


def is_valid_password(password):
    password = password.split(':')
    a, b, c = password[0], int(password[1]), int(password[2])
    if len(password) != 3 or a != a[::-1] or c % 2 != 0:
        return False
    for i in range(2, b):
        if b % i == 0:
            return False
    return True


psw = input()

print(is_valid_password(psw))


# --------Скобочная последовательность-----------
def is_correct_bracket(text):
    count = 0
    for i in text:
        if i == '(':
            count += 1
        elif i == ')':
            count += -1
            if count < 0:
                break
            return False
    return count == 0


def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return not text


def convert_to_python_case(text):
    from string import ascii_uppercase
    res = text[0].lower()
    for i in range(1, len(text)):
        if text[i] in ascii_uppercase:
            res += '_' + text[i].lower()
        else:
            res += text[i]
    return res


def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]


def convert_to_python_case(text):
    return ''.join(['_' + i if i.isupper() else i for i in text]).lstrip('_').lower()

