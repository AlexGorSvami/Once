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



def remove_all_before(items: list, border: int):
        if border in items:
            ind = items.index(border)
            del items[0:ind]
            return items
        else:
            return items
print(remove_all_before([2,3,2,1,0,4,5,5,5,6], 4))