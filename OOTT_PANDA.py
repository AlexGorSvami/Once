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


class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'


p1 = Person()
print(hasattr(p1.__dict__, 'job'))
