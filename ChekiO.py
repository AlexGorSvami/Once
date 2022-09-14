# def nearest_value(values: set, one: int):
#     if one in values:
#         return one
#     else:
#         values.add(one)
#         l1 = list(values)
#         l1.sort()
#         ind = l1.index(one)
#         try:
#             if one == 0:
#                 if ind == 0:
#                     return l1[ind + 1]
#                 else:
#                     return l1[ind -1]
#             elif one > 0:
#                 if abs(l1[ind]) - abs(l1[ind-1]) <= abs(l1[ind+1]) - abs(l1[ind]):
#                     return l1[ind-1]
#                 else:
#                     return l1[ind+1]
#             else:
#                 if abs(l1[ind]) - abs(l1[ind-1]) >= abs(l1[ind]) - abs(l1[ind+1]):
#                     return l1[ind+1]
#                 else:
#                     return l1[ind-1]
#         except IndexError:
#             return l1[ind-1]
#
#
#
# print(nearest_value({4, 7, 10, 11, 12, 17}, 8))
# print(nearest_value({4, 7, 10, 11, 12, 17}, 0))
# print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
# print(nearest_value({-6, -2, 4, 7, 12, 17}, -4))
# print(nearest_value({4, 7, 10, 11, 12, 17}, 100))
# print(nearest_value({-1,2,3},0))


# def nearest_value(values: set, one: int) -> int:
#     return min(sorted(values), key=lambda i: abs(i - one))
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(nearest_value({4, 7, 10, 11, 12, 17}



# def remove_all_before(items: list, border: int):
#         if border in items:
#             ind = items.index(border)
#             del items[0:ind]
#             return items
#         else:
#             return items
# print(remove_all_before([2,3,2,1,0,4,5,5,5,6], 4))
#
# def remove_all_before(items, border):
#     try:
#         return items[items.index(border):]
#     except ValueError:
#         return items
#
# remove_all_before=lambda i,b:b in i and i[i.index(b):] or i
#
#
# def remove_all_before(items: list, border: int) -> Iterable:
#     return items[items.index(border):] if border in items else items

# [data[i] for i in range(len(data) if i == data.index(data[i])]

# def checkio( data) :
#     data= [i for i in data if data.count(i) >= 2]
#     return data
#
# checkio=lambda d:[x for x in d if d.count(x)>1]
#
# checkio = lambda d: list(filter(lambda i: d.count(i) - 1, d))
#
# def checkio(data):
#     from collections import Counter
#     nonunique = Counter(data) - Counter(set(data))
#     return [x for x in data if x in nonunique]
#
# print(checkio([1, 2, 3, 1, 3]))


# a,b,c = map(int, input().split())
# print(max(a,b,c)**2 == (min(a,b,c)**2) + ((a+b+c) - max(a,b,c) - min(a,b,c))**2)

# f = sorted(map(int,input().split()))
# print(f[0]**2 + f[1]**2 == f[2]**2)

# a,b,c=map(int,input().split())
# print(a**2+b**2+c**2-max(a,b,c)**2==max(a,b,c)**2)