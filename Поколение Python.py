# ------------------------------------------------- Ревью--------------------------------------------------

# count = 0
# p = 1
# for i in range(1,11):
#     x = int(input())
#     if x > -1:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')
#
#
# mx = -9999999999
# s = 0
# for i in range(1,11):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > mx:
#             mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')
#
# s = 0
# for _ in range(1, 8):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# print(s)
#
# n = int(input())
# while n > 9:
#     n //= 10
# print(n)
#
# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)


# --------------------------------Тема урока: вложенные циклы-----------------------------------------

n = int(input())
for i in range(1,n+1):
    for j in range(5):
        print(i, end=' ')
    print()


n = int(input())
for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()


n = int(input())
for i in range(n//2+2):
    print('*' * i)
for i in range(n//2,0,-1):
    print('*' * i)


n = int(input())

for i in range(n):
    k = (n // 2 + 1) - abs(n // 2 - i)
    for _ in range(k):
        print('*', end='')
    print()

