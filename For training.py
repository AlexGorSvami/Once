# print(1,2,3, end = " ")
# print(7,8,9)


# a = int(input())
# b = int(input())
# if a < b:
#     for i in range(a,b+1):
#        print(i,end = " ")
# else:
#     for i in range(a,b-1,-1):
#         print(i, end = " ")

# c = int(input())
# d = int(input())
# for j in range(c - (c +1) % 2,d - d % 2,-2):
#     print(j, end = " ")

# s = 0
# for i in range(10):
#     s += int(input())
# print(s)

# n = int(input())
# s = 0
# for _ in range(n):
#     s += int(input())
# print(s)

# N = int(input())
# summ = 0
# for i in range(1, N + 1):
#         summ += i ** 3
# print(summ)

# n = int(input())
# f = 1 
# for i in range(1, n + 1):
#     f *= i
# print(f)

# n = int(input())
# f = 1 
# summ = 0
# for i in range(1, n + 1):
#     f *= i
#     summ += f
# print(summ)

# N = int(input())
# cnt = 0

# for _ in range(N):
#     p = int(input())
#     if p == 0:
#         cnt +=1
# print(cnt)

# a = int(input())

# for c in range(1, a + 1):
#     for q in range(1, c + 1):
#         print(q, end = "")
#     print()
# n = int(input())
# st = ""
# for i in range(1,n + 1):
#     st += str(i)
#     print(st)

# from re import I


# N = int(input())
# s1 = 0
# s2 = 0
# for i in range(1,N+1):
#     s1 += i
# for _ in range(N - 1):
#     s2 += int(input())
# print(s1 - s2)

# for i in range(10+1):
#      for j in range(i, i + 1):
#          print(j,end = "")
#      print()

# n = int(input())
# count = 0
# for i in range(1,n):
#     count += int(input())
# print(count())

# n = int(input())
# print(n< 100 and range(15,n,15) or ['слишком большое значение n'])


import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
print(lst_in)
i = 0
while i < len(lst_in):
    if ' ' in lst_in[i]:
        lst_in.remove(lst_in[i])
    i += 1

print(*lst_in)