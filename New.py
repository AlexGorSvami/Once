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


n = int(input())
mas = [[int(j) for j in input().split()] for i in range(n)]
count = 0
for i in range(n):
    mid = sum(mas[i]) / len(mas[i])
    for j in range(n):
        if mas[i][j] > mid:
            count += 1
    print(count)
    count = 0

