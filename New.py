# n = int(input())
# h = (n // 60) % 24
# print(h, n % 60)
#
# num = int(input())
# end ='.'
# print('The next number for the number', str(num), 'is', str(num+1)+'.')
# print ('The previous number for the number', str(num), 'is', str(num-1)+'.')

# a,b,c = int(input()),int(input()),int(input())
# print((a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2))
#
# a,b,l,N = int(input()),int(input()),int(input()),int(input())
# print(2*l+(2*N-1)*a+2*(N-1)*b)

# a,b,c,d = int(input()),int(input()),int(input()),int(input())
# if (a+b) % 2 == 0 and (c+d) % 2 == 0 or (a+b) % 2 != 0 and (c+d) % 2 != 0:
#     print('YES')
# else:
#     print('NO')

# my_str = 'Valera'
#
# new_str = my_str[len(my_str)//2-1:len(my_str)//2+1]
#
# print(new_str)


# def end_zeros(a: int) -> int:
#     zer = 0
#     a = str(a)
#     for i in a[::-1]:
#         if int(i) == 0:
#             zer += 1
#         else:
#             break
#     return zer
#
# print(end_zeros(1000))
#
# def end_zeros(number):
#     n = str(number)
#     return len(n) - len(n.strip('0'))
#
# def end_zeros(number):
#     number = str(number)
#     if number[-1:] != '0':
#         return 0
#     return 1 + end_zeros(number[:-1])


# def index_power(list_, number) -> int:
#     if number > len(list_):
#         return -1
#     else:
#         return list_.pop(number) ** number
#
# print(index_power([1,2,3], 2))

# def between_markers(text: str, start: str, end: str) -> str:
#     s = text.find(start)
#     l = text.find(end)
#     return text[s:l:].strip(start)
#
# print('Example:')
# print(between_markers('What is >apple<', '>', '<'))

# def replace_first(items: list):
#     new = 1
#     if len(items) == 0 or len(items) == 1 or len(items) == 2:
#         return items
#     else:
#         items[0] = new
#         items.pop(0)
#         items.append(new)
#     return items
#
# def replace_first(lst):
#     if len(lst):
#         lst.append(lst.pop(0))
#     return lst
#
# replace_first = lambda l: l[1%len(l):]+l[:1%len(l)] if not len(l)==0 else l
#
#
# from typing import Iterable
# import numpy as np
#
# def replace_first(items: list) -> Iterable:
#     # your code here
#     return np.roll(items,-1)
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(list(replace_first([1, 2, 3, 4])))

# def correct_sentence(text: str) -> str:
#     return text.replace(text[0], text[0].upper(), 1)
#
# print('Example:')
# print(correct_sentence("greetings, friends"))

# def best_stock(data: dict[str, float]) -> str:
#     for i, j in data.items():
#         if j == max(data.values()):
#             return i
#
#
# print("Example:")
# print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))


# def nearest_value(values: set, one: int) -> int:
#     if one in values:
#         return one
#     else:
#         for i in values:
#             if
#
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(nearest_value({4, 7, 10, 11, 12, 17}, 9))


# a, b = map(int, input().split())
# print((a+b-2)-(a-1), (a+b-2)-(b-1))
#
# a = int(input())
# b = int(input())
# c = int(input())
# print(max((a+b+c), (a*b*c), (a*(b+c)), ((a+b)*c), (a*b + c), (a + b * c)))

# def nearest_value(values: set, one: int) -> int:
#     if one in values:
#         return one
#     else:

# assert nearest_value({4, 7, 10, 11, 12, 17}, 9)


# mas = [float(i) for i in input().split()]
# for i, el in enumerate(mas):
#     if  el < 0:
#         mas[i] = -1.0
#
# print(mas)

# list1 = [[1] * 3] * 3
# print(list1)
# list1[0][1] = 5
# print(list1)


# class SoccerPlayer:
#     def __init__(self, name, surname, goals=0, assists=0) -> None:
#         self.name = name
#         self.surname = surname
#         self.goals = goals
#         self.assists = assists
#
#     def score(self, goals=1):
#         self.goals += goals
#
#     def make_assist(self, assists=1):
#         self.assists += assists
#
#     def statistics(self):
#         print(f'{self.surname}{self.name}-голы {self.goals}, передачи: {self.assists}')
#
#
# leo = SoccerPlayer('Leo', 'Messi')
# leo.score(700)
# leo.make_assist(500)
# leo.statistics() # выводит "Messi Leo - голы: 700, передачи: 500"
# kokorin = SoccerPlayer('Alex', 'Kokorin')
# kokorin.score()
# kokorin.statistics() # выводит "Kokorin Alex - голы: 1, передачи: 0"


# n = int(input())
# print(*[list(range(1,n+1)) for i in range(n)],sep='\n')

# n = 4
# mas = []
# for i in range(n):
#     mas.append([1] * n)
#
# for i in range(n):
#     for j in range(n):
#         if j == n-1:
#             mas[i][j] = 5
#
# for i in mas:
#     print(*i)


# glas = 'йуеыэаояию'
# a = input()
# g = 0
# s = 0
# for i in a:
#     if i in glas:
#         g += 1
#     elif i.isalpha():
#         s += 1
# print(g, s, sep='\n')


# s = input()
# ords = 0
# for i in range(len(s)):
#     ords += ord(s[i])
# mas = []
# if len(s) == 8:
#     for i in s:
#         for j in s:
#             for k in s:
#                 for l in s:
#                     for m in s:
#                         for n in s:
#                             for o in s:
#                                 for r in s:
#                                     res = i + j + k + l + m + n + o + r
#                                     if res not in mas:
#                                         if ord(i) + ord(j) + ord(k) + ord(l) + ord(m) + ord(n) + ord(o) + ord(
#                                                 r) == ords:
#                                             mas.append(res)
# if len(s) == 7:
#     for i in s:
#         for j in s:
#             for k in s:
#                 for l in s:
#                     for m in s:
#                         for n in s:
#                             for o in s:
#                                 res = i + j + k + l + m + n + o
#                                 if res not in mas:
#                                     if ord(i) + ord(j) + ord(k) + ord(l) + ord(m) + ord(n) + ord(o) == ords:
#                                         mas.append(res)
# if len(s) == 6:
#     for i in s:
#         for j in s:
#             for k in s:
#                 for l in s:
#                     for m in s:
#                         for n in s:
#                             res = i + j + k + l + m
#                             if res not in mas:
#                                 if ord(i) + ord(j) + ord(k) + ord(l) + ord(m) + ord(n) == ords:
#                                     mas.append(res)
#
# if len(s) == 5:
#     for i in s:
#         for j in s:
#             for k in s:
#                 for l in s:
#                     for m in s:
#                         res = i + j + k + l + m
#                         if res not in mas:
#                             if ord(i) + ord(j) + ord(k) + ord(l) + ord(m) == ords:
#                                 mas.append(res)
#
# if len(s) == 4:
#     for i in s:
#         for j in s:
#             for k in s:
#                 for l in s:
#                     res = i + j + k + l
#                     if res not in mas:
#                         if ord(i) + ord(j) + ord(k) + ord(l) == ords:
#                             mas.append(res)
#
# if len(s) == 3:
#     for i in s:
#         for j in s:
#             for k in s:
#                 res = i + j + k
#                 if res not in mas:
#                     if ord(i) + ord(j) + ord(k) == ords:
#                         mas.append(res)
#
# if len(s) == 2:
#     for i in s:
#         for j in s:
#             res = i + j
#             if res not in mas:
#                 if ord(i) + ord(j) == ords:
#                     mas.append(res)
#
# if len(s) == 1:
#     mas.append(s)
#
# print(*sorted(mas), sep='\n')


# n = int(input())
# mas = [[1]*n]*n
# for i in range(n):
#     mas[i][-1] = 5
#
# for i in mas:
#     print(*i)


# lst_in = ['django chto  eto takoe    poryadok ustanovki','model mtv   marshrutizaciya funkcii  predstavleniya marshrutizaciya  obrabotka isklyucheniy', 'zaprosov perenapravleniya']
#
# for i,v in  enumerate(lst_in) :
#     while ' ' in v:
#         v = v.replace(' ','-')
#         while '--' in v:
#            v=v.replace('--','-')
#     lst_in[i] = v
#     print(lst_in[i], end='\n')


# n = int(input())
# print(2,end=' ')
# for i in range(3,n+1):
#     if i % 2 != 0:
#         print(i,end=' ')
#

# def polindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return polindrom(s[1:-1])
#
#
# s = input().split()
# res = []
# for i in s:
#     if len(i) > 2 and polindrom(i):
#         res.append(i)
#
# print(*sorted(res))

# n = int(input())
# mas = [[1]*n]*n
# mas[0][n-1] = 5
# for i in mas:
#     print(*i)
#
#
# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# for i in lst_in:
#     print('-'.join(i.split()))

# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# for line in lst_in:
#     while '  ' in line:
#         line = line.replace('  ', ' ')
#     line = line.replace(' ', '-')
#     print(line)

# n =  221
#
# n = int(input())
# while n != 0:
#     print(n // 64,end='  ')


# mas = [int(i) for i in input().split()]
# print(max(mas),min(mas),(mas[len(mas)//2] + mas[(len(mas)-1)//2])/2)

# from math import sqrt
#
#
# class Point:
#
#     list_points = []
#     def __init__(self, x=0, y=0):
#         self.move_to(x, y)
#         Point.list_points.append(self)
#
#     def move_to(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#
#     def go_home(self):
#         self.move_to(0, 0)
#
#     def print_point(self):
#         print(self.x, self.y)
#
#     def calc_distance(self, another_point):
#         if not isinstance(another_point, Point):
#             raise ValueError('Argument not touch')
#
#         return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)
#
#
# p7 = Point(6, 0)
# p8 = Point(0, 8)
# p11 = Point(1,12)
#
# print(Point.list_points[1].x)


# class Person:
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age
#
#     def display_person_info(self):
#         print(f'Person: {self.name}, {self.age}')
#
# class Company:
#     def __init__(self,company_name, location):
#         self.company_name = company_name
#         self.location = location
#
#     def display_company_info(self):
#         print(f'Company: {self.company_name}, {self.location}')
#
# class  Employee:
#     def __init__(self,name,  age, company_name, location):
#         self.personal_data  = Person(name,age)
#         self.work =  Company(company_name, location)
#
#
# emp = Employee('Jessica', 28, 'Google', 'Atlanta')
# print(emp.personal_data.name)
# print(emp.personal_data.age)
# emp.personal_data.display_person_info()
# print(emp.work.company_name)
# print(emp.work.location)
# emp.work.display_company_info()

# mas = [64,32,16, 8, 4,2,1]
# res = []
# n = 221
# for i in mas:
#     while n - i >= 0:
#         res.append(i)
#         n -= i
# print(*res)

# n = 7
# p = []
#
# for i in range(n):
#     row = [1] * (i + 1)
#     for j in range(i+1):
#         if j != 0 and j != i:
#             row[j] = p[i-1][j-1] + p[i-1][j]
#     p.append(row)
#
# for r in p:
#     print(*r)


# def PrintPasriangle(rows):
#     row = [1]
#     for i in range(rows):
#         print(row)
#         row = [sum(x) for x in zip([0] + row, row+[0])]
#
# PrintPasriangle(10)


# b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
#      'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# s = input()
# res = s + ' запретил букву '
# for i in b:
#     while i in res:
#         print(res + i)
#         res = res.replace(i, '')
#         res = res.lstrip()
#         res = res.replace('  ',' ')

# n = 4
# [print(*[1 if i == j else 0 for j in range(n)]) for i in range(n)]

# n = 4
# [print(*[*[i] * n]) for i in range(n)]
#
#
# l = input().split()
# print([[l[i-1],int(l[i])] for i in range(1,len(l),2)])


# # Напишите определение класса Rectangle
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#
# # Ниже код для проверки методов класса Rectangle
# r1 = Rectangle(2, 3)
# assert r1.width == 2
# assert r1.height == 3
# assert r1.perimeter() == 10
# assert r1.area() == 6
#
# r2 = Rectangle(10, 0.5)
# assert r2.width == 10
# assert r2.height == 0.5
# assert r2.perimeter() == 21.0
# assert r2.area() == 5.0
# print('Good')


# class WeatherStation:
#     __shared_atribute = {
#         "temperature": 0, "humidity": 0, "pressure": 0
#     }
#     def __init__(self):
#         self.__dict__ = WeatherStation.__shared_atribute
#
#     def update_data(self, *args):
#         for i, key in enumerate(WeatherStation.__shared_atribute):

#
# n = int(input())
# mas = [[int(j) for j in input().split()] for i in range(n)]
# count = 0
# for i in range(n):
#     mid = sum(mas[i]) / len(mas[i])
#     for j in range(n):
#         if mas[i][j] > mid:
#             count += 1
#     print(count)
#     count = 0


# l = [i.split('=') for i in input().split()]
# for i in range(len(l)):
#     l[i][1] = int(l[i][1])
# d = dict(l)
# print(*sorted(d.items()))

# d = dict(c.split('=') for c in input().split())
# for c in d:
#   d[c] = int(d[c])
# print(*sorted(d.items()))


# lst = [i.split('=') for i in input.split()]
# d = {i: int(v) for i, v in lst}
# print(*sorted(d.items()))


# ls = [i.split('=') for i in input().split()]
# d = {i:val for i, val in ls}
# if  'house' in d and 'True' in d and '5' in d:
#     print('ДА')
# else:
#     print('НЕТ')


# d = dict([i.split('=') for i in input().split()])
# print('ДА' if 'house' in d and 'True' in d and '5' in d else 'НЕТ')

# lst = input().split()
# d = {}
# for i in lst:
#     key = i[:2]
#     if key not in d:
#         d[key] = []
#     d[key].append(i)
#
# print(*sorted(d.items()))

# import sys
#
# # считывание списка из входного потока
# ls = list(map(str.strip, sys.stdin.readlines()))
# d = {}
# for i in range(len(ls)):
#     ls[i] = ls[i].split()
#     key = ls[i][1]
#     if key not in d:
#         d[key] = []
#     d[key].append(ls[i][0])
#
# print(*sorted(d.items()))


# n = int(input())
# d = {}
# while n != 0:
#     if n not in d:
#         d[n] = round(n**0.5, 2)
#     else:
#         print(f'значение из кэша: {d[n]}')
#     n = int(input())

# morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ё': '.', 'ж': '...-', 'з': '--..',
#              'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
#              'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
#              'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
#
# word = 'Сергей Балакирев'
# res = ''
# for i in word:
#     if i.lower() in morze:
#         res +=morze[i.lower()] + ' '
# print(res.strip())


# morze = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', 'ж': '...-', 'з': '--..',
#          'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.',
#          'с': '...', 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
#          'щ': '--.-', 'ъ': '--.--', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-', ' ': '-...-'}
# reversed_morze = {v: k for k, v in morze.items()}
# print(reversed_morze)
# kod = input().split()
# for i in kod:
#     print(reversed_morze[i], end='')


# numbers = [int(i) for i in input().split()]
# res = dict.fromkeys(numbers)
# print(*res.keys())

# print(*dict.fromkeys(input().split()))


import sys


# считывание списка из входного потока
# ls = list(map(str.strip, sys.stdin.readlines()))
#
# dic = {}
# for i in ls:
#     key, val = i.split()
#     if key not in dic:
#         dic[key] = []
#     dic[key].append(val)
#
# [print(*[key + ':', ', '.join(val)]) for key, val in dic.items()]


# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# max_weight = int(input())*1000
# res = []
# #
# for key, val in sorted(things.items(), key=lambda x: -x[1]):
#     if max_weight - val >= 0:
#         max_weight -=val
#         res.append(key)
#     else:
#         continue
#
# print(res)

# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

# d = {}
# for i in lst_in:
#     if i not in d:
#         d[i] = i
#         print(f'HTML-страница для адреса {d[i]}')
#     else:
#         print(f'Взято из кэша: HTML-страница для адреса {d[i]}')


# import sys
#
# # считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# # здесь продолжайте программу (используйте список lst_in)
# used = {}
# for line in lst_in:
#     print(f'{used.get(line,"")}HTML-страница для адреса {line}')
#     used[line] = 'Взято из кэша: '


# t = tuple(input().split())
# t = tuple(i.lower() for i in t if 'ва' in i.lower())
# print(*t)

# t = tuple(map(int, input().split()))
# t1 = []
# for i in  t:
#     if i not in t1:
#         t1.append(i)
#
#
# tup = tuple(input().split())
# tup2 = ()
#
# for i in tup:
#     if i not in tup2:
#         tup2 += i,

# non_unic = tuple(input().split())
# print(*(i for i,val in enumerate(non_unic) if non_unic.count(val) >  1 ))


# n = int(input())
# t = ((1, 0, 0, 0, 0),
#      (0, 1, 0, 0, 0),
#      (0, 0, 1, 0, 0),
#      (0, 0, 0, 1, 0),
#      (0, 0, 0, 0, 1))
# for i in range(n):
#     print(*t[i][:n])

# import sys
#
# # считывание списка из входного потока
# ls = list(map(str.strip, sys.stdin.readlines()))
#
# print(tuple(tuple(i.split()) for i in ls ))

# res = {int(i) for i in input() if i.isdigit()}
# print(*sorted(res) if len(res) > 0 else {'НЕТ'})


# ls = ['EvgeniyK: спасибо большое!',
# 'LinaTroshka: лайк и подписка!',
# 'Sergey Karandeev: крутое видео!',
# 'Евгений Соснин: обожаю',
# 'EvgeniyK: это повтор?',
# 'Sergey Karandeev: нет, это новое видео']
# lst = [i.split(':')[0] for i in ls]
# print(len(set(lst)))


# mas =  input().split()
# d = {int(ind):val for ind,val in enumerate(mas[1:],int(mas[0]))}
# print(d[4])
#
# start, *names = input().split()
# print(dict(enumerate(names, int(start)))[4])
#
# mas = input().lower().split()
# keys = {i for i in mas}
# d = {i:mas.count(i) for i in keys}
# print(d.get('и', 0))
#
#
# lst = input().lower().split()
# print({w: lst.count(w) for w in set(lst)}.get('и', 0))

# ls = ['Пушкин: Сказака о рыбаке и рыбке',
#       'Есенин: Письмо к женщине',
#       'Тургенев: Муму',
#       'Пушкин: Евгений Онегин',
#       'Есенин: Русь']
#
# # d = {}
# # for i in ls:
# #     key, value = i.split(': ')
# #     d.setdefault(key, set()).add(value)
#
# d = {i.split(':')[0] : {j.split(': ')[1] for j in ls if i.split()[0] == j.split()[0]} for i in ls}`
# print(d)

# def chet(x):
#     return not x % 2
#
# [print(i) for i in iter(input, '1') if chet(int(i))]
#
#
# def not_even(num:int)->int:
#     return num % 2
# print(*[int(i) for i in input().split() if not_even(int(i))])
#
# class Library:
#     def __init__(self, books: list):
#         self.__books = books
#
#     def __check_availability(self, book):
#         return book in self.__books
#
#
#     def search_book(self, book):
#         return self.__check_availability(book)
#
#     def return_book(self,book):
#         self.__books.append(book)
#
#     def _checkout_book(self, book):
#         if book in self.__books:
#             self.__books.remove(book)
#             return True
#         return False
#
#
# library = Library(["War and Peace", "Moby-Dick", "Pride and Prejudice"])
#
# assert library._Library__books == ["War and Peace", "Moby-Dick", "Pride and Prejudice"]
# assert library.search_book("Moby-Dick") == True
# assert library.search_book("Jane Air") == False
#
# assert library._Library__check_availability("War and Peace") == True
# assert library._checkout_book("Moby-Dick") == True
# assert library._Library__books == ["War and Peace", "Pride and Prejudice"]
#
# assert library.search_book("Moby-Dick") == False
# assert library.return_book("Moby-Dick") is None
# assert library._Library__books == ["War and Peace", "Pride and Prejudice", "Moby-Dick"]
# assert library.search_book("Moby-Dick") == True
# print('Good')


# class Employee:
#     def __init__(self, name, position, hours_worked, hourly_rate):
#         self.name = name
#         self.__position = position
#         self.__hours_worked = hours_worked
#         self.__hourly_rate = hourly_rate
#
#     def __calculate_salary(self):
#         return self.__hours_worked * self.__hourly_rate
#
#     def _set_position(self, position):
#         self.__position = position
#
#     def get_position(self):
#         return self.__position
#
#     def get_salary(self):
#         return self.__calculate_salary()
#
#     def get_employee_details(self):
#         return f"Name: {self.name}, Position: {self.__position}, Salary: {self.__calculate_salary()}"
#
#
# employee = Employee("Джеки Чан", 'manager', 20, 40)
# assert employee.name == 'Джеки Чан'
# assert employee._Employee__hours_worked == 20
# assert employee._Employee__hourly_rate == 40
# assert employee._Employee__position == 'manager'
# assert employee.get_position() == 'manager'
# assert employee.get_salary() == 800
# assert employee._Employee__calculate_salary() == 800
# assert employee.get_employee_details() == 'Name: Джеки Чан, Position: manager, Salary: 800'
# employee._set_position('Director')
# assert employee.get_employee_details() == 'Name: Джеки Чан, Position: Director, Salary: 800'
#
# employee_2 = Employee("Пирс Броснан", 'actor', 35, 30)
# assert employee_2._Employee__calculate_salary() == 1050
# assert employee_2.get_employee_details() == 'Name: Пирс Броснан, Position: actor, Salary: 1050'
#
# print('Good')

# print(*sorted({i:len(i) for i in input().split()},key=lambda x: len(x)))
#
# def twin(x):
#     return x, len(x)
# d= {k:v for k,v in map(twin, input().split())}
# a = sorted(d, key=lambda x: d[x])
# print(a)


# def get_len(s):
#     return s, len(s)
# d = dict(get_len(i) for i in input().split())
# print(*sorted(d, key=lambda x: d[x]))


# from collections import deque
#
# lst_in = list(map(int, input().split()))
# q = deque()
# q.extend(lst_in)
# for i in range(3):
#     print(q.popleft(),end=' ')
#
#
# from collections import deque
#
# lst_in = list(map(str.strip, input().split()))
# q = deque()
# q.extend(lst_in)
# q.insert(2,'run')
# q.remove('edit')

# from collections import deque
#
# data = list(map(int, input().split()))
# fifo = deque()
# for i in data:
#     fifo.appendleft(i)
# print(*[fifo.pop() for i in range(3)])


# from collections import deque
#
# data = [1, 3, 4, 5, 6, 7, 8, 9, 0, 7, 6, 4, 3,]
# buff = deque(maxlen=10)
# buff.extendleft(data)
# print(*[buff.pop() for i in range(3)])

# data = list(map(int, input().split()))
# lifo = [i for i in data]
# print(*[lifo.pop() for i in range(2)])


# def get_nod(a, b):
#     if b > a:
#         a, b = b, a
#     while  b != 0:
#         a, b = b, a % b
#     return a
#
# print(get_nod(15, 121050))

# t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
#      'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
#     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
#     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
#
# def ru_en(st, sep='-'):
#     return ''.join([t[i] if i in t else sep if i == ' ' else i for i in st])
#
# st = input().lower()
# print(ru_en(st))
# print(ru_en(st, sep='+'))


# def get_data_fig(*args, **kwargs):
#     per = 0
#     for i in args:
#         per += i
#     res = [per]
#     if 'type' in kwargs:
#         res.append(kwargs['type'])
#     if 'color' in kwargs:
#         res.append(kwargs['color'])
#     if 'closed' in kwargs:
#         res.append(kwargs['closed'])
#     if 'width' in kwargs:
#         res.append(kwargs['width'])
#
#     return (tuple(res))


# def get_data_fig(*args, **kwargs):
#     kwargs = [kwargs[i] for i in ['type', 'color', 'closed', 'width'] if i in kwargs]
#     return (sum(args), *kwargs)
#
#
# print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))
# print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
# print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))


# lst_c = *input().split(),
# print(lst_c)
#
#
# numbers, cities = map(float, input().split()), input().split()
# lst = [*numbers, *cities]
# print(*lst)

# class BankAccount:
#
#     def __init__(self,account_number, balance):
#         self._account_number = account_number
#         self._balance = balance
#
#     def get_account_number(self):
#         return self._account_number
#
#     def get_balance(self):
#         return self._balance
#
#     def set_balance(self, value):
#         self._balance = value
#
# account = BankAccount("1234567890", 1000)
# assert account._balance == 1000
# assert account._account_number == "1234567890"
# assert account.get_account_number() == "1234567890"
# assert account.get_balance() == 1000
# account.set_balance(1500)
# assert account.get_balance() == 1500
#
# print('Good')


# N = int(input())
#
# def get_rec_N(N):
#     if N > 1:
#         get_rec_N(N-1)
#     print(N)

# def get_rec_sum(mas:list)->int:
#     if len(mas) == 1:
#         return mas[0]
#     return mas[0]  + get_rec_sum(mas[1:])
#
# mas = list(map(int, input().split()))
# print(get_rec_sum(mas))


# N = int(input())
#
# def fib_rec(N, f=[1, 1]):
#     if len(f) < N:
#         f.append(f[-1] + f[-2])
#         fib_rec(N, f)
#     return f

#
# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
#
# def get_line_list(d,a=[]):
#     # if a == None:
#     #     a = []
#     for i in d:
#         if type(i) != list:
#             a.append(i)
#         else:
#             get_line_list(i)
#     return a
#
# print(get_line_list(d))


# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
#
#     def __get_name(self):
#         return self.__name
#
#     def __get_salary(self):
#         return self.__salary
#
#     def __set_salary(self, value):
#         if (type(value) ==  float or type(value) == int) and value > 0:
#             self.__salary = value
#         else:
#             print(f'ErrorValue:{value}')
#
#     title = property(
#         fget=__get_name)
#
#     reward = property(
#         fget=__get_salary,
#         fset=__set_salary
#     )
#
#
# # Ниже код для проверки методов класса Employee
# employee = Employee("John Doe", 50000)
# assert employee.title == "John Doe"
# assert employee._Employee__name == "John Doe"
# assert isinstance(employee, Employee)
# assert isinstance(type(employee).title, property), 'Вы не создали property title'
# assert isinstance(type(employee).reward, property), 'Вы не создали property reward'
#
# assert employee.reward == 50000
# employee.reward = -100  # ErrorValue:-100
#
# employee.reward = 1.5
# assert employee.reward == 1.5
#
# employee.reward = 70000
# assert employee.reward == 70000
# employee.reward = 'hello'  # Печатает ErrorValue:hello
# employee.reward = '777'  # Печатает ErrorValue:777
# employee.reward = [1, 2]  # Печатает ErrorValue:[1, 2]
# assert employee.reward == 70000
# employee._Employee__set_salary(55000)
# assert employee._Employee__get_salary() == 55000


class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if '.' in value and '@' in value and value.count('@') == 1 and value.index('.') > value.index('@'):
            self.__email = value
        else:
            print(f'ErrorMail:{value}')

    email = property(fget=get_email, fset=set_email)


jim = UserMail("aka47", 'hello@com.org')
assert jim.login == "aka47"
assert jim._UserMail__email == "hello@com.org"
assert isinstance(jim, UserMail)
assert isinstance(type(jim).email, property), 'Вы не создали property email'

jim.email = [1, 2, 3]  # печатает ErrorMail:[1, 2, 3]
jim.email = 'hello@@re.ee'  # печатает ErrorMail:hello@@re.ee
jim.email = 'hello@re.w3'
assert jim.email == 'hello@re.w3'

k = UserMail('belosnezhka', 'prince@wait.you')
assert k.email == 'prince@wait.you'
assert k.login == 'belosnezhka'
assert isinstance(k, UserMail)

k.email = {1, 2, 3}  # печатает ErrorMail:{1, 2, 3}
k.email = 'prince@still@.wait'  # печатает ErrorMail:prince@still@.wait
k.email = 'prince@stillwait'  # печатает ErrorMail:prince@stillwait
k.email = 'prince@still.wait'
assert k.get_email() == 'prince@still.wait'
k.email = 'pri.nce@stillwait'  # печатает ErrorMail:pri.nce@stillwait
assert k.email == 'priince@still.wait'


