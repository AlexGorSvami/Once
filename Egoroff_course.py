# a,b,c = map(int, input().split())# print(a,b,c,end='',sep=',')## a=int(input())# print((a-1),a,(a+1),sep=' < ')## a = int(input())# print('%s < %s < %s'%(a-1, a, a+1))## n = int(input())# print(f'{n - 1} < {n} < {n + 1}')# import math# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')# print('Основатель', 'Питона', sep='_', end='!')# n = 56789# print(n // 100 % 10)### print(sum(map(int,input())))# n = int(input())# print((n // 100) + (n % 100 // 20) + (n % 100 % 20 // 10) + (n % 100 % 20 % 10 // 5) + (n % 100 % 20 % 10 % 5 // 1))### n = int(input()) % 1440# print(n // 60, n % 60)### n = int(input())# print(n // 60 % 24, n % 60)## n = int(input())# print(n + 2 - n % 2)# n = int(input())# hours = n // 3600# minutes = n % 3600 // 60# seconds = n % 3600 % 60# print(f'{hours}:{minutes // 10 % 10}{minutes % 10}:{seconds // 10 % 10}{seconds % 10}')# from math import ceil## print(sum([ceil(int(input()) / 2) for _ in range(3) ]))## import math# print(math.ceil(int(input())/4))# print('Я стану крутым программистом!\n'*3# a,b,c = map(str, input().split())# print(f'Simvol code {a} is {ord(a)}.')# print(f'Simvol code {b} is {ord(b)}.')# print(f'Simvol code {c} is {ord(c)}.')# [print(f'Simvol code {el} is {ord(el)}.') for el in input().split()]# print(input().rfind('a'))# print(input().find('a'))## print(len(input().split()))# s = 'PYTHON'## print(a[0:3].upper()+ a[3:-3].lower() + a[-3:-1:1].upper()+a[-1].upper())## a =(input().lower()).replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')# print('.' + '.'.join(a))# phrase = input().upper().split()# print('-'.join(phrase[0]), '-'.join(phrase[1]))## print(*map('-'.join, input().upper().split()))## phrase = input().split()# print('\n'.join(phrase))## print('\n'.join(input().split()))## print(*input().split(), sep='\n')# a = int(input())# if (a // 100000 + a // 10000 % 10 + a // 1000 % 10) == (a // 100 % 10 + a // 10 % 10 + a % 10):#     print('YES')# else:#     print('NO')### a = list(map(int, input()))# if sum(a[-3:]) == sum(a[:-3]):#     print("YES")# else:#     print("NO")# s = ' abcdefg'# coord_1, coord_2 = input(), input()# letter_1, letter_2 = coord_1, coord_2# column_1, column_2 = s.find(letter_1[0]), s.find(letter_2[0])# row_1, row_2 = int(coord_1[1]), int(coord_2[1])# if (column_1 + row_1) % 2 == (column_2 + row_2) % 2:#     print('YES')# else:#     print('NO')# maximum = int(input())# minimum = int(input())# print(minimum, maximum) if minimum < maximum else print (maximum,minimum)# a,b,c=sorted(map(int, input().split()))# print(c-a)# s, v1,v2,t1,t2 = map(int, input().split())# time1 = s*v1 + t1*2# time2 = s*v2 + t2*2# print('First' if time1 < time2 else 'Second' if time1 > time2 else 'Friendship')# a,b=input().lower().replace('ь',''),input().lower()# print('Good' if a[-1]==b[0] else 'Bad')# m = input()# n = int(m)# print('Fizz' * (not n % 3) + 'Buzz' * (not n % 5) or m)### n = int(input())# print((n, 'Fizz', 'Buzz', 'FizzBuzz')[(not n % 3) + 2 * (not n % 5)])# abc = {input(), input(), input()}# print(0 if len(abc) == 3 else 4 - len(abc))# n = int(input())# month = ['Январь', 'Февраль', 'Март', 'Апрель',#          'Май', 'Июнь', 'Июль', 'Август',#          'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']# print(month[n-1])# print([0, 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'][int(input())])# match int(input()):#     case 1:#         print('Совсем еще зеленый студентик')#     case 2:#         print('Джун-студент')#     case 3:#         print('Мидл-студент')#     case 4:#         print('Сеньер-студент')#     case 5:#         print('Босс качалки')#     case _:#         print('Неизвестный курс')# a, b = map(int, input().split())# y = 0# while a <= b:#     a, b, y = a * 3, b * 2, y + 1# print(y)# X,Y = map(int, input().split())# count = 1# while X < Y:#     X += 15 * X /100#     count +=1# print(count)# n,m = map(int, input().split())# day = 0# while n > 0:#     n -= 1#     day += 1#     if day % m  == 0:#         n += 1# print(day)# num = int(input())# i = 0# while 2**i < num:#     i += 1# if 2 **i == num:#     print(i)# else:#     print('НЕТ')# n = int(input())# first = int(str(n)[0])# while first != 1 and n < 10**9:#     first = int(str(n)[0])#     n *= first## print(n)## summ = 0# while (n := int(input())) != 0:#     summ += n# print(summ)## i = int(input())# level = 0# cub_level = 0# s = 0# while s < i:#     level += 1#     cub_level += level#     s += cub_level#     if s == i:#         print(level)# print(level-1)# n,m = map(int, input().split())# list1 = list(map(int, input().split()))# list2 = list(map(int, input().split()))# i = j = 0# answer = []# while i < n and j < m:#     if list1[i] < list2[j]:#         answer.append(list1[i])#         i += 1#     else:#         answer.append(list2[j])#         j += 1# while i < n:#     answer.append(list1[i])#     i += 1# while j < m:#     answer.append(list2[j])#     j += 1## print(*answer)## n, m = map(int,input().split())# s = list(map(int,input().split())) + list(map(int,input().split()))# c = []# while len(s) > 0:#     c.append(min(s))#     s.remove(min(s))# print(*c)# m, y, w, x = [sorted([*map(int,input().split())]) for i in range(4)]# for i in y:#     for j in x:#         if abs(i-j) <= 1:#             x.remove(j)# print(w[0]-len(x))# x = 3456# count = 0# count_chet = 0# count_nech = 0# summ = 0# while x > 0:#     last = x % 10#     count += 1#     if last % 2 == 0:#         count_chet +=1#     else:#         count_nech +=1#     summ += last#     x //= 10# print(count, count_nech, count_nech, summ)# ПОИСК ВСЕХ ДЕЛИТЕЛЕЙ ЧИСЛА:# n = int(input())# i = 1# while i <= n:#   if n % i == 0:#       print(i, end=' ')#       i += 1# n = int(input())# i = 1# while i <= n // 2 :#   if n % i == 0:#       print(i, end=' ')#       i += 1## n = int(input())# res = []# i = 1# while i*i <= n:#     if n % i == 0:#         res.append(i)#         if i != n // i:#             res.append(n//i)#     i += 1# res.sort()# print(sum(res))# n = int(input())# count = 0# i = 1# while i*i <= n:#     if n % i == 0:#         if i == n // i:#             count += 1#         else:#             count += 2#     i += 1# if count != 2:#     print('No')# else:#     print('Yes')                    # НАХОЖДЕНИЕ НОД(АЛГОРИТМ ЕВКЛИДА)# a, b = map(int, input().split())# while a != b:#     if a > b:#         a =a - b#     else:#         b = b - a                    # НАХОЖДЕНИЕ НОK(АЛГОРИТМ ЕВКЛИДА)# a, b = map(int, input().split())# a1, b1 = a, b# while 0 < b:#     a, b = b, a % b# print(a1 * b1 // a)import math## print(math.lcm(a, b))# a = int(input())# b = int(input())# while a <= b:#     if a == 777:#         break#     if a % 2 == 0 or a % 3 == 0:#         a += 1#         continue#     print(a)#     a += 1## a, b = int(input()), int(input()) + 1# while a < b:#     if a == 777:#         break#     if a % 2 and a % 3:#         print(a)#     a += 1# Гипотеза Сиракуз:## n = int(input())# count = 0# while n != 1:#     if n % 2 == 0:#         n =n / 2#         count += 1#     else:#         n = n * 3 + 1#         count += 1# print(count)### n, cnt = int(input()), 0# while n != 1:#     n = n // 2 if n % 2 == 0 else 3 * n + 1#     cnt += 1# print(cnt)# word = input()# i = 0# while i != len(word):#     if word[i] == 'e' or word[i] == 'a':#         print('Ага! Нашлась')#         break#     print(f'Текущая буква: {word[i]}')#     i += 1# else:#     print('Распечатали все буквы')#### a = list(input())# while a:#     if a[0] == 'a' or a[0] == 'e':#         print('Ага! Нашлась')#         break#     else:#         print(f'Текущая буква: {a[0]}')#         a = a[1:]#         if a == []:#             print('Распечатали все буквы')## x=input().replace('a','e').split('e')# print('\nТекущая буква: '.join(' '+ x[0])[2:])# print(['Распечатали все буквы','Ага! Нашлась'][len(x)>1])# for n in range(int(input()), int(input()) + 1):#     print('Fizz' * (not n % 3) + 'Buzz' * (not n % 5) or n)# a,b = int(input()), int(input())# for i in range(a,b+1):#     print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')## print(sum(i for i in range(int(input())) if not i % 3 or not i % 5))