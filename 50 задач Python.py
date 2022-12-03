# a = list(map(int,input().split()))
# a = sorted(a)
# for i in range(len(a)-1):
#     if a[i] == a[i+1]:
#         print(a[i])


# import numpy as np
# a = str(input()).split(' ')
# a = np.array([int(item) for item in a])
# counter = {}
#
# for elem in a:
#     counter[elem] = counter.get(elem, 0) + 1
#
# doubles = {element: count for element, count in counter.items() if count > 2}
# for i in sorted(doubles.keys()):
#     print(i)


# a = list(map(int, input().split()))
# counter = {}
# for elem in a:
#     counter[elem] = counter.get(elem, 0) + 1
#
# doubles = {element: count for element, count in counter.items if count > 2}
# for i in sorted(doubles.keys()):
#     print(i)

a = [1, 3, 4, 5, 3, 3, 44, 1, 14, 15, 4, 1, 44]
new = []
[new.append(i) for i in a if i not in new]
print(*new)