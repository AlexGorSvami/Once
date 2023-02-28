# class Goods:
#     title = 'Мороженное'
#     weight = 154
#     tp = 'Еда'
#     price = 1024
#
#
# Goods.price = 2048
# Goods.inflation = 100
# print(Goods.__dict__)
# print(Goods().inflation)


# class Car:
#     pass
#
#
# setattr(Car, 'model', 'Тойота')
# setattr(Car, 'color', 'Розовый')
# setattr(Car, 'number', 'П111ГУУ77')
#
# print(Car.__dict__['color'])


# class Notes:
#     uid = 1005435
#     title = 'Шутка'
#     author = 'И.С.  Бах'
#     pages = 2
#
#
# print(getattr(Notes,'author'))


# class Dictionary:
#     rus = 'Питон'
#     eng = 'Python'
#
#
# print(getattr(Dictionary, 'rus_word', False))


# class TravelBlog:
#     total_blogs = 0
#
#
# tb1 = TravelBlog()
# tb1.name = 'Франция'
# tb1.days = 6
#
# TravelBlog.total_blogs += 1
#
# tb2 = TravelBlog()
# tb2.name = 'Италия'
# tb2.days = 5
#
# TravelBlog.total_blogs += 1
#
# print(TravelBlog.__dict__)
# print(tb1.__dict__)
# print(tb2.__dict__)


# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
#
# fig1 = Figure()
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = 'blue'
#
# del fig1.color
# print(*[key for key, values in fig1.__dict__.items()])
#
#
# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
#
# fig1 = Figure()
#
# fig1.__dict__.update({'start_pt': (10, 5), 'end_pt': (100, 20), 'color': 'blue'})
# del fig1.color
#
# print(*fig1.__dict__)


# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
#
# p1 = Person()
# print(hasattr(p1.__dict__, 'job'))


# class Notes:
#     uid = 1005435
#     title = 'Шутка'
#     author = 'И.С. Бах'
#     pages = 2
#
# print(getattr(Notes,'author'))

# class TravelBlog:
#     total_blogs = 0
#
#
# tb1 = TravelBlog()
# tb1.name = 'Франция'
# tb1.days = 6
#
# TravelBlog.total_blogs += 1
#
# tb2 = TravelBlog()
# tb2.name = 'Италия'
# tb2.days = 5
#
# TravelBlog.total_blogs += 1


# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
#
# fig1 = Figure()
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = 'blue'
#
# del fig1.color
#
# for key,val in fig1.__dict__.items():
#     print(key,end=' ')

# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'
#
#
# p1 = Person()
# print(hasattr(p1.__dict__, 'job'))

# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#     def play(self):
#          print(f"Воспроизведение {self.filename}")
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
#
# media1.open('filemedia1')
# media2.open('filemedia2')
#
# media1.play()
# media2.play()

# class Graph:
#     def set_data(self, data):
#         self.data =  data
#
#     def draw(self,LIMIT_Y = [0, 10]):
#         for i in self.data:
#             if i in range(11):
#                 print(i,end=' ')
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()


# import sys
#
# class StreamData:
#     def create(self,fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         for i, key  in enumerate(fields):
#             setattr(self, key, lst_values[i])
#
#         return True
#
# class StreamReader:
#     FIELDS = ('id', 'title', 'pages')
#
#     def readlines(self):
#         lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
#         sd = StreamData()
#         res = sd.create(self.FIELDS, lst_in)
#         return sd, res
#
#
# sr = StreamReader()
# data, result = sr.readlines()

# class MediaPlayer:
#     def open(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
#
# media1.open('filemedia1')
# media2.open('filemedia2')
#
# media1.play()
# media2.play()

# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         print(' '.join(map(str, filter(lambda x: self.LIMIT_Y[0] <= x <= self.LIMIT_Y[-1], self.data))))
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()


# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         a, b = self.LIMIT_Y
#         print(*filter(lambda x: a <= x <= b, self.data))
#
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()


# class Graph:
#     LIMIT_Y = [0, 10]
#     def set_data(self, data):
#         self.data = data
#     def draw(self):
#         start, end = self.LIMIT_Y
#         res = (i for i in self.data if i in range(start, end+1))
#         print(*res)
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()

# class StreamData:
#     def create(self, fields, lst_values):
#         if len(fields) != len(lst_values):
#             return False
#         for i, key in enumerate(fields):
#             setattr(self, key, lst_values[i])
#
#         return True
#
# class StreamData:
#     def create(self, fields, lst_values):
#         self.__dict__ = dict(zip(fields, lst_values))
#         return len(lst_values) == len(fields)

import sys

# lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


# class DataBase:
#     lst_data = []
#     FIELDS = ('id', 'name', 'old', 'salary')
#
#     def insert(self,data):
#         for x in data:
#             self.lst_data.append(dict(zip(self.FIELDS, x.split())))
#
#     def select(self,a,b):
#         return self.lst_data[a:b+1]
#
# db = DataBase()
# db.insert(lst_in)
# print(db.select(0,1))

# class Translator:
#     def add(self, eng, rus):
#         if 'tr' not in self.__dict__:
#             self.tr = {}
#         self.tr.setdefault(eng, [])
#         if rus not in self.tr[eng]:
#             self.tr[eng].append(rus)
#
#     def remove(self, eng):
#         self.tr.pop(eng, False)
#
#     def translate(self, eng):
#         return self.tr[eng]
#
# tr = Translator()
# tr.add("tree", "дерево")
# tr.add("car", "машина")
# tr.add("car", "автомобиль")
# tr.add("leaf", "лист")
# tr.add("river", "река")
# tr.add("go", "идти")
# tr.add("go", "ехать")
# tr.add("go", "ходить")
# tr.add("milk", "молоко")
#
# tr.remove('car')
# print(*tr.translate('go'))


# class Money:
#     def __init__(self, money):
#         self.money = money

# class Point:
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#
# points = [Point(i, i, 'yellow') if i == 3 else Point(i, i) for i in range(1, 2000, 2)]


# from random import randint
# class Line:
#     def __init__(self, a, b, c, d, ):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d, ):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d, ):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# elements = [(Line, Rect, Ellipse)[randint(0,2)] (1,2,3,4) for n in range(217)]
# for obj in elements:
#     if isinstance(obj, Line):
#         obj.sp = obj.ep = 0, 0

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if not all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c))):
#             return 1
#         if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
#             return 1
#         a, b, c = self.a, self.b, self.c
#         if a >= b + c or b >= a + c or c >= a + b:
#             return 2
#         return 3


# a, b, c = map(int, input().split())
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())


# здесь объявляются все необходимые классы
# class Graph:
#     def __init__(self, data, is_show=True):
#         self.data = data[:]
#         self.is_show = is_show
#
#     def set_data(self, data):
#         setattr(self.data, data)
#
#     def show_table(self):
#         if self.is_show:
#             print(*self.data)
#         else:
#             print('Отображение данных закрыто')
#
#     def show_graph(self):
#         if self.is_show:
#             print('Графическое отображение данных:', *self.data)
#         else:
#             print('Отображение данных закрыто')
#
#     def show_bar(self):
#         if self.is_show:
#             print('Столбчатая диаграмма:', *self.data)
#         else:
#             print('Отображение данных закрыто')
#
#     def set_show(self, fl_show):
#         self.is_show = fl_show
# # считывание списка из входного потока (эту строку не менять)
# data_graph = list(map(int, input().split()))
#
# # здесь создаются объекты классов и вызываются нужные методы
# gr = Graph(data_graph)
# gr.show_bar()
# gr.set_show(fl_show = False)
# gr.show_table()

# class CPU:
#     def __init__(self,name,fr):
#         self.name = name
#         self.fr = fr
#
# class Memory:
#     def __init__(self, name, volume):
#         self.name = name
#         self.volume = volume
#
# class MotherBoard:
#     def __init__(self,name, cpu, *mems):
#         self.name = name
#         self.cpu = cpu
#         self.total_mem_slots = 4
#         self.mem_slots = mems[:self.total_mem_slots]
#
#     def get_config(self):
#         return [f'Материнская плата: {self.name}',
#                     f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
#                     f'Слотов памяти: {self.total_mem_slots}',
#                     'Память: ' + '; '.join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]
#
#
# mb = MotherBoard('Gigabyte', CPU('Intel', 2000), Memory('Kingston', 1000), Memory('Kingston', 1000))

#
# class  Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self,indx):
#         self.goods.pop(indx)
#
#     def get_list(self):
#         return [f'{x.name}: {x.price}' for x in self.goods]
#
#
# class Table:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class TV:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
# class Notebook:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class Cup:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# cart = Cart()
# tv1 = TV("samsung", 1111)
# tv2 = TV("LG", 1234)
# table = Table("ikea", 2345)
# n1= Notebook("msi", 5433)
# n2 = Notebook("apple", 542)
# c = Cup("keepcup", 43)
#
# cart.add(tv1)
# cart.add(tv2)
# cart.add(table)
# cart.add(n1)
# cart.add(n2)
# cart.add(c)
#
# class ListOdject:
#     def __init__(self, data):
#         self.data = data
#         self.next_obj = None
#
#     def link(self, obj):
#         self.next_obj = obj
#
#
# head_obj = ListOdject(lst_in[0])
# obj = head_obj
# for x in range(1, len(lst_in)):
#     obj_new = ListOdject(lst_in[i])
#     obj.link(obj_new)
#     obj = obj_new
from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N, M):
        self._n = N
        self._m = M
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
        self.init()

    def init(self):
        m = 0
        while m < self._m:
            i = randint(0, self._n - 1)
            j = randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            self.pole[i][j].mine = True
            m += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    mines = sum((self.pole[x + i][y + j].mine for i, j in indx if
                                 0 <= x + i < self._n and 0 <= y + j < self._n))
                    self.pole[x][y].around_mines = mines

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.show()
