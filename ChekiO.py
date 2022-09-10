# values = {-6, -2, 4, 7, 12, 17}
# one = -4
# if one in values:
#     print(one)
# else:
#     values.add(one)
#     l1 = list(values)
#     l1.sort()
#     ind = l1.index(one)
#     if one > 0:
#         abs(l1[ind]) - abs(l1[ind-1]) >= abs(l1[ind]) - abs(l1[ind+1]):
#             print(l1[ind-1])
#     else:
#         print(l1[+1])

# def nearest_value(values: set, one: int):
#     if one in values:
#         return one
#     else:
#         values.add(one)
#         l1 = list(values)
#         l1.sort()
#         ind = l1.index(one)
#         if abs(l1[ind]) - abs(l1[ind-1]) >= abs(l1[ind]) - abs(l1[ind+1]):
#             return l1[ind-1]
#         else:
#             return l1[ind+1]
#
# assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
# assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
# assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
# assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
# assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
# assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
# assert nearest_value({5}, 5) == 5

def nearest_value(values: set, one: int):
    if one in values:
        return one
    else:
        values.add(one)
        l1 = list(values)
        l1.sort()
        ind = l1.index(one)
        if abs(l1[ind]) - abs(l1[ind-1]) >= abs(l1[ind]) - abs(l1[ind+1]):
            return l1[ind-1]
        else:
            return l1[ind+1]

print(nearest_value({4, 7, 10, 11, 12, 17}, 8))
print(nearest_value({-6, -2, 4, 7, 12, 17}, -4))