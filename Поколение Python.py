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

# n = int(input())
# for i in range(1,n+1):
#     for j in range(5):
#         print(i, end=' ')
#     print()
#
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()
#
#
# n = int(input())
# for i in range(n//2+2):
#     print('*' * i)
# for i in range(n//2,0,-1):
#     print('*' * i)
#
#
# n = int(input())
#
# for i in range(n):
#     k = (n // 2 + 1) - abs(n // 2 - i)
#     for _ in range(k):
#         print('*', end='')
#     print()


# n = int(input())
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i, end='')
#     print()
#

# total = 0
# for n in range(15):
#     for k in range(10):
#         for m in range(10):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 total +=1
#                 print(n,k,m)
#                 print(total)


# n = int(input())
# num = 1
# for row in range(1,n+1):
#     for col in range(1,row+1):
#         print(num, end=' ')
#         num +=1
#     print()


# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,end='')
#     for k in range(i-1,0,-1):
#         print(k,end='')
#     print()
#
# a = int(input())
# b = int(input())
# summ = 0
# maxx = 0
# for x in range(a,b+1):
#     count = 0
#     for i in range(1,x+1):
#         if x % i == 0:
#             count +=i
#             if count >= summ:
#                 summ = count
#                 maxx = x
# print(maxx, summ)


# n = int(input())
# while n > 9:
#     n = n // 10 + n % 10
# print(n)

# number = int(input())
#
# total = 0
#
# while number > 9:
#     while number != 0:
#         total += number % 10
#         number //= 10
#     number, total = total, 0
#
# print(number)


# n = int(input())
# answer = 0
# fact = 1
# for i in range(1,n+1):
#     fact *= i
#     i -= 1
#     answer +=fact
# print(answer)


# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     count = 0
#     for j in range(1,i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i)

# n = int(input())
# count3 = 0
# last = n % 10
# lastcount = 0
# chetcount = 0
# sum_ = 0
# more7 = 1
# count05 = 0
# while n > 0:
#     last1 = n % 10
#     if last1 == 3:
#         count3 +=1
#     if last1 == last:
#         lastcount += 1
#     if last1 % 2 == 0:
#         chetcount += 1
#     if last1 > 5:
#         sum_ += last1
#     if last1 > 7:
#         more7 *= last1
#     if last1 == 0 or last1 == 5:
#         count05 += 1
#             n //=10
# print(count3)
# print(lastcount)
# print(chetcount)
# print(sum_)
# print(more7)
# print(count05)

# for a in range(1,34):
#     for b in range(1,34):
#         for c in range(1, 34):
#             for d in range(1, 34):
#                 if a **3 + b **3 == c**3 + d**3 and  a != b and a != c and a != d and b != c and b != d and c != d:
#                     print(a**3 + b**3)

s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')


print('Цифра' if [i for i in input() if i.isdigit()] else 'Цифр нет')

