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