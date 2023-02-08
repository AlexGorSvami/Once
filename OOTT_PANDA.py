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

lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']


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

class Line:
    def __init__(self,a,b,c,d,):
        self.sp = a,b
        self.ep = c,d
class Rect:
    def __init__(self,a,b,c,d,):
class Ellipse:
    def __init__(self,a,b,c,d,):

