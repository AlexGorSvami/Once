# n = int(input())
# count = 0
# for i in range(n):
#     count += int(input())
# print(count)

# def s(a, *vs, b=10):
#     res = a + b
#     for v in vs:
#         res +=  v
#     return res
#
# print(s(11,b=20))
# print(s(11,10))
# print(s(21))
# print(s())

# mas = [int(i) for i in input().split()]
# mas.sort()
# print(*mas[:3])

mas = [[int(j) for j in input().split()] for i in range(3)]
for i in mas:
    print(i[3],end=' ')