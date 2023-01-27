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


class Car:
    pass


setattr(Car, 'model', 'Тойота')
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', 'П111ГУУ77')

print(Car.__dict__['color'])
