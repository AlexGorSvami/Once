# a,b,c = map(int, input().split())# print(a,b,c,end='',sep=',')## a=int(input())# print((a-1),a,(a+1),sep=' < ')## a = int(input())# print('%s < %s < %s'%(a-1, a, a+1))## n = int(input())# print(f'{n - 1} < {n} < {n + 1}')# import math# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')# print('Основатель', 'Питона', sep='_', end='!')# n = 56789# print(n // 100 % 10)### print(sum(map(int,input())))# n = int(input())# print((n // 100) + (n % 100 // 20) + (n % 100 % 20 // 10) + (n % 100 % 20 % 10 // 5) + (n % 100 % 20 % 10 % 5 // 1))### n = int(input()) % 1440# print(n // 60, n % 60)### n = int(input())# print(n // 60 % 24, n % 60)## n = int(input())# print(n + 2 - n % 2)# n = int(input())# hours = n // 3600# minutes = n % 3600 // 60# seconds = n % 3600 % 60# print(f'{hours}:{minutes // 10 % 10}{minutes % 10}:{seconds // 10 % 10}{seconds % 10}')# from math import ceil## print(sum([ceil(int(input()) / 2) for _ in range(3) ]))## import math# print(math.ceil(int(input())/4))# print('Я стану крутым программистом!\n'*3# a,b,c = map(str, input().split())# print(f'Simvol code {a} is {ord(a)}.')# print(f'Simvol code {b} is {ord(b)}.')# print(f'Simvol code {c} is {ord(c)}.')# [print(f'Simvol code {el} is {ord(el)}.') for el in input().split()]# print(input().rfind('a'))# print(input().find('a'))## print(len(input().split()))# s = 'PYTHON'## print(a[0:3].upper()+ a[3:-3].lower() + a[-3:-1:1].upper()+a[-1].upper())## a =(input().lower()).replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','')# print('.' + '.'.join(a))# phrase = input().upper().split()# print('-'.join(phrase[0]), '-'.join(phrase[1]))## print(*map('-'.join, input().upper().split()))## phrase = input().split()# print('\n'.join(phrase))## print('\n'.join(input().split()))## print(*input().split(), sep='\n')# a = int(input())# if (a // 100000 + a // 10000 % 10 + a // 1000 % 10) == (a // 100 % 10 + a // 10 % 10 + a % 10):#     print('YES')# else:#     print('NO')### a = list(map(int, input()))# if sum(a[-3:]) == sum(a[:-3]):#     print("YES")# else:#     print("NO")# s = ' abcdefg'# coord_1, coord_2 = input(), input()# letter_1, letter_2 = coord_1, coord_2# column_1, column_2 = s.find(letter_1[0]), s.find(letter_2[0])# row_1, row_2 = int(coord_1[1]), int(coord_2[1])# if (column_1 + row_1) % 2 == (column_2 + row_2) % 2:#     print('YES')# else:#     print('NO')# maximum = int(input())# minimum = int(input())# print(minimum, maximum) if minimum < maximum else print (maximum,minimum)# a,b,c=sorted(map(int, input().split()))# print(c-a)# s, v1,v2,t1,t2 = map(int, input().split())# time1 = s*v1 + t1*2# time2 = s*v2 + t2*2# print('First' if time1 < time2 else 'Second' if time1 > time2 else 'Friendship')# a,b=input().lower().replace('ь',''),input().lower()# print('Good' if a[-1]==b[0] else 'Bad')# m = input()# n = int(m)# print('Fizz' * (not n % 3) + 'Buzz' * (not n % 5) or m)### n = int(input())# print((n, 'Fizz', 'Buzz', 'FizzBuzz')[(not n % 3) + 2 * (not n % 5)])# abc = {input(), input(), input()}# print(0 if len(abc) == 3 else 4 - len(abc))# n = int(input())# month = ['Январь', 'Февраль', 'Март', 'Апрель',#          'Май', 'Июнь', 'Июль', 'Август',#          'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']# print(month[n-1])# print([0, 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'][int(input())])# match int(input()):#     case 1:#         print('Совсем еще зеленый студентик')#     case 2:#         print('Джун-студент')#     case 3:#         print('Мидл-студент')#     case 4:#         print('Сеньер-студент')#     case 5:#         print('Босс качалки')#     case _:#         print('Неизвестный курс')# a, b = map(int, input().split())# y = 0# while a <= b:#     a, b, y = a * 3, b * 2, y + 1# print(y)# X,Y = map(int, input().split())# count = 1# while X < Y:#     X += 15 * X /100#     count +=1# print(count)# n,m = map(int, input().split())# day = 0# while n > 0:#     n -= 1#     day += 1#     if day % m  == 0:#         n += 1# print(day)# num = int(input())# i = 0# while 2**i < num:#     i += 1# if 2 **i == num:#     print(i)# else:#     print('НЕТ')# n = int(input())# first = int(str(n)[0])# while first != 1 and n < 10**9:#     first = int(str(n)[0])#     n *= first## print(n)## summ = 0# while (n := int(input())) != 0:#     summ += n# print(summ)## i = int(input())# level = 0# cub_level = 0# s = 0# while s < i:#     level += 1#     cub_level += level#     s += cub_level#     if s == i:#         print(level)# print(level-1)# n,m = map(int, input().split())# list1 = list(map(int, input().split()))# list2 = list(map(int, input().split()))# i = j = 0# answer = []# while i < n and j < m:#     if list1[i] < list2[j]:#         answer.append(list1[i])#         i += 1#     else:#         answer.append(list2[j])#         j += 1# while i < n:#     answer.append(list1[i])#     i += 1# while j < m:#     answer.append(list2[j])#     j += 1## print(*answer)## n, m = map(int,input().split())# s = list(map(int,input().split())) + list(map(int,input().split()))# c = []# while len(s) > 0:#     c.append(min(s))#     s.remove(min(s))# print(*c)# m, y, w, x = [sorted([*map(int,input().split())]) for i in range(4)]# for i in y:#     for j in x:#         if abs(i-j) <= 1:#             x.remove(j)# print(w[0]-len(x))# x = 3456# count = 0# count_chet = 0# count_nech = 0# summ = 0# while x > 0:#     last = x % 10#     count += 1#     if last % 2 == 0:#         count_chet +=1#     else:#         count_nech +=1#     summ += last#     x //= 10# print(count, count_nech, count_nech, summ)# ПОИСК ВСЕХ ДЕЛИТЕЛЕЙ ЧИСЛА:# n = int(input())# i = 1# while i <= n:#   if n % i == 0:#       print(i, end=' ')#       i += 1# n = int(input())# i = 1# while i <= n // 2 :#   if n % i == 0:#       print(i, end=' ')#       i += 1## n = int(input())# res = []# i = 1# while i*i <= n:#     if n % i == 0:#         res.append(i)#         if i != n // i:#             res.append(n//i)#     i += 1# res.sort()# print(sum(res))# n = int(input())# count = 0# i = 1# while i*i <= n:#     if n % i == 0:#         if i == n // i:#             count += 1#         else:#             count += 2#     i += 1# if count != 2:#     print('No')# else:#     print('Yes')# НАХОЖДЕНИЕ НОД(АЛГОРИТМ ЕВКЛИДА)# a, b = map(int, input().split())# while a != b:#     if a > b:#         a =a - b#     else:#         b = b - a# НАХОЖДЕНИЕ НОK(АЛГОРИТМ ЕВКЛИДА)# a, b = map(int, input().split())# a1, b1 = a, b# while 0 < b:#     a, b = b, a % b# print(a1 * b1 // a)import math## print(math.lcm(a, b))# a = int(input())# b = int(input())# while a <= b:#     if a == 777:#         break#     if a % 2 == 0 or a % 3 == 0:#         a += 1#         continue#     print(a)#     a += 1## a, b = int(input()), int(input()) + 1# while a < b:#     if a == 777:#         break#     if a % 2 and a % 3:#         print(a)#     a += 1# Гипотеза Сиракуз:## n = int(input())# count = 0# while n != 1:#     if n % 2 == 0:#         n =n / 2#         count += 1#     else:#         n = n * 3 + 1#         count += 1# print(count)### n, cnt = int(input()), 0# while n != 1:#     n = n // 2 if n % 2 == 0 else 3 * n + 1#     cnt += 1# print(cnt)# word = input()# i = 0# while i != len(word):#     if word[i] == 'e' or word[i] == 'a':#         print('Ага! Нашлась')#         break#     print(f'Текущая буква: {word[i]}')#     i += 1# else:#     print('Распечатали все буквы')#### a = list(input())# while a:#     if a[0] == 'a' or a[0] == 'e':#         print('Ага! Нашлась')#         break#     else:#         print(f'Текущая буква: {a[0]}')#         a = a[1:]#         if a == []:#             print('Распечатали все буквы')## x=input().replace('a','e').split('e')# print('\nТекущая буква: '.join(' '+ x[0])[2:])# print(['Распечатали все буквы','Ага! Нашлась'][len(x)>1])# for n in range(int(input()), int(input()) + 1):#     print('Fizz' * (not n % 3) + 'Buzz' * (not n % 5) or n)# a,b = int(input()), int(input())# for i in range(a,b+1):#     print(f'Число {i}; его квадрат = {i**2}; его куб = {i**3}')## print(sum(i for i in range(int(input())) if not i % 3 or not i % 5))## summ = 0# for i in range(50,101):#     summ += i**3# print(summ)# n = int(input())# a = 1# for i in range(1, n + 1):#     a *= i# print(a)# ## n = int(input())# mscore=0# cscore=0# for i in range(0,n):#     m, c=map(int,input().split())#     if m > c:#         mscore += 1#     elif c > m:#         cscore += 1# if mscore>cscore:#     print('Mishka')# elif cscore>mscore:#     print('Cris')# else:#     print("Friendship is magic!^^" )## for i in range(int(input())):#     s = input()#     if 'рок' in s.lower():#         print(i+1, s.find('рок')+1 )# n = int(input())# result = []# for i in range(n):#     a = input()#     answer = ''#     if 'соль' not in a:#         result.append(a)#         for i in result:#             answer += i + ', '# print(answer[:-2])# s = [input() for i in range(int(input()))]# print(*[i for i in s if not 'соль' in i], sep=', ')## n = int(input())# res = []# for i in range(n):#     s = input()#     if s not in 'соль':#         res.append(s)# print(", ".join(res))# n = int(input())# for i in range(n):#     s = input()#     if len(s) > 10:#         print(s[0] + str(len(s) - 2) + s[-1])#     else:#         print(s)# words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',#            'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',#            'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',#            'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',#            'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',#            'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',#            'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',#            'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',#            'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']# for i in range(len(words)):#     if len(words[i]) > 6:#         print(words[i])## n = int(input())# a = [input() for _ in range(n)]# print(a)# list = list(map(int, input().split()))# r = int(input())# for i in range(len(list)):#     if list[i] == r:#         print(i+1)#         break# else:#   print('ErrorValue')# print((lambda l, v: [i for i, k in enumerate(l, 1) if k == v][0] if v in l else 'ErrorValue')(input().split(), input()))# ls = list(map(int, input().split()))# res = 9999# for i in range(len(ls)):#     if ls[i] > 0 and ls[i] < res:#         res = ls[i]# if res == 9999:#     print('Empty')## else:#     print(res)# s = list(map(int, input().split()))# m = max(s)# for i in s:#     if i < m and i > 0:#         m = i# if m > 0:#     print(m)# else:#     print('Empty')# print((sorted([i for i in map(int, input().split()) if i > 0]) + ['Empty'])[0])# word = input().lower()# n = 0# n_max = 0# for i in range(len(word)):#     if n_max < n:#         n_max = n#         n = 0#     else:#         n = 0#     for value in word:#         if value == word[i]:#             n += 1# print(n_max)# a = input().lower()# kol = []# for i in a:#     kol.append(a.count(i))# print(max(kol))# n = str(int(input()))# ch = 0# nech = 0# for i in range(len(n)):#     if i % 2 == 0:#         ch += int(n[i])#     else:#         nech += int(n[i])# if (ch - nech) % 11 == 0:#     print('YES')# else:#     print('NO')# n = [int(i) for i in input()]# print('NO' if (sum(n[1::2]) - sum(n[0::2])) % 11 else 'YES')# n = input()# kol = 0# sum = 0# for i in range(len(n)):#     if n[i] in '0123456789':#         kol += 1#         sum +=int(n[i])# print(kol, sum)## a = [int(i) for i in input() if i.isdigit()]# print(len(a), sum(a))# n = list(input())# if n.count('(') == n.count(')'):#     print('YES')# else:#     print('NO')## a = input()# print('YES' if a.count('(') == a.count(')') else 'NO')# s = set()# for i in input().split():#     if i.lower() not in s:#         s.add(i.lower())#         print(i, end=' ')# import random## a = []# for i in range(10):#     a.append(random.randint(-10, 10))## count = [0] * 21# for i in a:#     count[i+10] += 1# print(a)## for i in range(21):#     if count[i] > 0:#         print(i-10, count[i])# s = input()# stack = []# flag = True# for i in s:#     if i in '([{':#         stack.append(i)#     elif i in ')]}':#         if not stack:#             flag = False#             break#         open = stack.pop()#         if open == '(' and i == ')':#             continue#         if open == '[' and i == ']':#             continue#         if open == '{' and i == '}':#             continue#         flag = False#         break## if flag and len(stack) == 0:#     print('YES')# else:#     print('NO')## pattern = input()# for i in range(len(pattern) // 2):#     pattern = pattern.replace('{}', '')#     pattern = pattern.replace('()', '')#     pattern = pattern.replace('[]', '')# print('YES' if len(pattern) == 0 else 'NO')## n = 436436## a = [0] * 10# for i in str(n):#     digit = int(i)#     a[digit] += 1## for i in range(10):#     if a[i] > 0:#         print(i, a[i])# n = input()# for i in range(10):#     if str(i) in n:#         print(i, n.count(str(i)))# n = int(input())# ls = list(map(int, input().split()))# count = [0] * 201# for i in ls:#     count[i + 100] += 1# for i in range(201):#     if count[i] > 0:#         print((str(i - 100) + ' ') * count[i], end='')# sum1 = 0# for i in range(1, 10000):#     x = i#     s = 0#     while x > 0:#         s += x % 10#         x //= 10#     if s == 20 and i > 999:#         sum1 += i#         print(sum1)#         print(i,s)### n = int(input())# for i in range(1,n+1):#     for j in range(1,i+1):#         print(j, end=' ')#     print( )##     l = list(map(int, input().split()))#     for i in l:#         print(i * '*')# n = int(input())# count = 0# for p in range(n + 1, 2 * n):#     if p % 2 == 0 and p != 2 or p == 1:#         continue#     d = 3#     is_plain = True#     while d * d <= p:#         if p % d == 0:#             is_plain = False#             break#         d += 2#     if is_plain:#         count += 1# print(count)# n = int(input())# a = 0# for i in range(n + 1, n * 2):#     for j in range(2, int(i ** 0.5) + 1):#         if i % j == 0:#             break#     else:#         a += 1# print(a)# n = 6# mas = [5, 7, 4, 3, 8, 2]# count = 0# for run in range(n-1):#     for i in range(n - 1-run):#         if mas[i] > mas[i + 1]:#             count += 1#             mas[i], mas[i + 1] = mas[i + 1], mas[i]# print(*mas)# print(count)## n, m = map(int, input().split())# a = 0# count = 0# while a ** 2 <= n:#     b = n - a ** 2#     if b >= 0 and a + b ** 2 == m:#         count += 1#     a += 1# print(count)## n,m = map(int, input().split())# print(sum(a+b*b == m and a*a+b == n for a in range(m+1) for b in range(n+1)))## list = []# for index in range(1,len(list)):#     value = list[index]#     i = index - 1#     while i >= 0:#         if value < list[i]:#             list[i + 1] = list[i]#             list[i] = value#             i = i - 1#         else:#             break# def is_plain_number(p):#     if p % 2 == 0 and p != 2 or p == 1:#         return False#     d = 3#     is_plain = True#     while d * d <= p:#         if p % d == 0:#             return False#         d += 2#     return True## n = int(input())# count = 0# for p in range(n + 1, 2 * n):#     if is_plain_number(p):#         count += 1# print(count)# n = 6# mas = [3, 1, 4, 6, 7, 2]# count = 0# for run in range(n-1):#     for i in range(n-1-run):#         if mas[i] > mas [i + 1]:#             count += 1#             mas[i], mas[i + 1] = mas[i + 1], mas[i]##     print(mas)# print(count)# Nested list# a = [[0, 2, 3, 4, 5], [1, 2, 4, 5], [2, 43, 5, 7, 8, [1, 2, 3, 4, 90]]]# print(len(a))# print(a[2][1])# print(a[0][4])# print(a[2][5][3])# b = ['hello', 'hi', 'world']# print(b[2][-1])# a = [#     [0, 2, 4, 6],#     [1, 5, 9, 23],#     [2, 45, 6, 87]# ]# for i in a:#     for j in i:#         j += 10#         print(j, end=' ')#     print()## print(a)# for j in range(4):#     for i in range(3):#         print(a[i][j], end=' ')#     print()# for i in range(2,-1,-1):#     for j in range(3, -1, -1):#         print(a[i][j], end=' ')#     print()# for j in range(4):#     s = 0#     for i in range(3):#         s += a[i][j]v#     print(s)## catalog = []# n = int(input())## for i in range(n):#     catalog.append([int(input)]*n)# for i in catalog:#     print(i)# a = []# n = int(input())# for i in range(n):#     b=[]#     for i in range(n):#         b.append(int(input()))#     a.append(b)# for i in a:#     print(i)# a = []# n = int(input())# for i in range(n):#     a.append([0] * n)## for i in range(n):#     for j in range(n):#         if i == j:#             a[i][j] = 10#         elif i > j:#             a[i][j] = 3#         else:#             a[i][j] = 5## for i in a:#     print(i)# ВЛОЖЕННЫЕ СПИСКИ# m = [list(map(int, input().split())) for _ in range(int(input()))]# s = 0# for i in range(len(m)):#     if m[i] == m[i]:#         s += m[i][i]# print(s)### n = int(input())# s = 0# for i in range(n):#     s += int(input().split()[i])# print(s)# print(sum(int(input().split()[i]) for i in range(int(input()))))# a = [list(map(int, input().split())) for _ in range(int(input()))]# for i in range(len(a)):#     for j in range(len(a)):#         print(a[j][i], end=' ')#     print()## s = int(input())# a = s // 6# print(a, 4*a, a)# a = hex(int(input())).lstrip('0x')# b = hex(int(input())).lstrip('0x')# c = hex(int(input())).lstrip('0x')## print('#',a.upper().zfill(2),b.upper().zfill(2),c.upper().zfill(2),sep='')# numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]# l = [111, 222, 789, 201]# numbers.append(111)# numbers.append(222)# numbers.append(789)# numbers.append(201)# print(numbers)# a = [list(map(int, input().split())) for _ in range(int(input()))]# for i in range(len(a)-1,-1,-1):#     for j in range(len(a)-1,-1,-1):#         print(a[j][i], end=' ')#     print()# n,m = map(int, input().split())# a = [list(map(int, input().split())) for _ in range(n)]# for i in range(n):#     for j in range(1,m+1):#         print(a[i][-j], end=' ')#     print()### n, _ = map(int, input().split())# for _ in range(n):#     print(*input().split()[::-1])## [print(*input().split()[::-1]) for i in range(int(input().split()[0]))]### n,m = map(int,input().split())# a = [list(map(int, input().split())) for _ in range(n)]# for i in range(n-1,-1,-1):#     for j in range(m):#         print(a[i][j], end=' ')#     print()# mas = []# for i in range(5):#     mas.append(list(map(int, input().split())))## for i in range(5):#     for j in range(5):#         if mas[i][j] == 1:#             row = i#             column = j## print(abs(2 - row) + abs(2 - column))## for i in range(5):#     a = list(input().split())#     if '1' in a:#         print(abs(a.index('1') - 2) + abs(i - 2))## n, m = map(int, input().split())# a = [list(map(int, input().split())) for _ in range(n)]# for i in range(n):#     s = 0#     for j in range(m):#         s += a[i][j]#     print(s, end=' ')# print()# for i in range(m):#     s1 = 0#     for j in range(n):#         s1 += a[j][i]#     print(s1, end=' ')## n, m = map(int, input().split())# matrix = [[int(i) for i in input().split()] for i in range(n)]# print(*[sum(i) for i in matrix])# print(*[sum(row[i] for row in matrix) for i in range(m)])## count = 0# n = int(input())# mas = [list(map(int, input().split())) for _ in range(n)]# for i in range(n):#     for j in range(n):#         if mas[i][j] != mas[j][i]:#             count += 1# if count > 0:#     print('No')# else:#     print('Yes')## n = int(input())# s = [input().split() for i in range(n)]# s1 = [[s[j][i] for j in range(n)] for i in range(n)]# print('Yes' if s == s1 else 'No')# a,b = map(int, input().split())# s = []# q = []# for i in range(a):#     s.append(list(map(int, input().split())))# for i in range(a):#         q.append(sum(s[i]))# print(max(q))# print(q.index(max(q)))## rows, cols = map(int, input().split())# matrix = [list(map(int, input().split())) for row in range(rows())]# answer = list(map(sum, matrix))# print(max(answer), answer.index(max(answer)), sep='\n')# n, m = map(int, input().split())# a = []# for i in range(n):#     row = list(map(int, input().split()))#     a.append(row)## maxim = 0# i_max = 0# j_max = 0# for i in range(n):#     for j in range(m):#         if maxim < a[i][j]:#             maxim = a[i][j]#             i_max = i#             j_max = j## print(maxim)# print(i_max, j_max)# n,m = map(int,input().split())# a = [list(map(int, input().split())) for _ in range(n)]# many = 0# best = 0# ind = 0# for i in range(n):#     max_try = 0#     s = 0#     for j in range(m):#         s += a[i][j]#         if a[i][j] > max_try:#             max_try = a[i][j]#     if max_try > best:#         best = max_try#         many = s#         ind = i#     elif max_try == best and s > many:#         best - max_try#         many = s#         ind = i# print(ind)# n,m = map(int, input().split())# a = [list(map(int, input().split())) for _ in range(n)]# best = 0# for i in range(n):#     max_try = 0#     for j in range(m):#         if a[i][j] > max_try:#             max_try = a[i][j]#     if max_try > best:#         best = max_try#         count = 1#     elif max_try == best:#         count += 1# print(count)# s = [[i for i in input()] for j in range(4)]# q = 'Yes'# for i in range(3):#     for j in range(3):#         if s[i][j] == s[i][j + 1] == s[i + 1]j == s[i+1][j+1]:#             q = 'No'# print(q)# n,m = map(int, input().split())# count = 0# original = [input() for i in range(n)]# input()# new = [input() for i in range(n)]# for i in range(n):#     for j in range(m):#         if original[i][j] == new[i][j]:#             count +=1# print(count)### n, x = map(int, input().split())# count = 0# for i in range(1, n + 1):#     for j in range(1, n + 1):#         if i * j == x:#             count += 1# print(count)# n = int(input())# count = 0# l = [list(map(int, input().split())) for i in range(n)]# for i in range(n):#     for j in range(n):#         if l[i][0]==l[j][1]:#             count += 1# print(count)# n, m = map(int, input().split())# mas = []# mas.append('.' * (m + 2))# for i in range(n):#     row = '.' + input() + '.'#     mas.append(row)# mas.append('.' * (m + 2))# k = 0# for i in range(1, n + 1):#     for j in range(1, m + 1):#         if mas[i - 1][j] == '.' and mas[i][j + 1] == '.' and mas[i + 1][j] == '.' and mas[i][j - 1] == '.' and mas[i][j] == '.':#             k += 1# print(k)# n, m = (int(i) for i in input().split())                 # ввод строки/стобцы# a = [[str(j) for j in input()] for i in range(n)]        # ввод поля боя# no_count = 0                                             # антисчетчик# count = 0                                                # счетчик годных клеток# for i in range(n):                                       # проход по строкам поля#     for j in range(m):                                   # в нем проход по столбцам#         if a[i][j] != '*':                               # если текущая клетка не корабль#             for d in (-1, 1):                            # то проход по соседям сверху-снизу + слева-справа#                 ai = i + d                               # и расчет адресов соседей сверху-снизу#                 if 0 <= ai < n and a[ai][j] == '*':      # и если сосед в рамках поля и это корабль#                         no_count += 1                    # тогда антисчетчик +1#                 aj = j + d                               # и расчет адресов соседей слева-справа#                 if 0 <= aj < m and a[i][aj] == '*':      # и если сосед в рамках поля и это корабль#                         no_count += 1                    # тогда антисчетчик +1#             count += 1 if no_count == 0 else 0           # если среди соседей нет кораблей то счетчик +1#             no_count = 0                                 # антисчетчик = 0 и обход поля до самого конца# print(count)# r,c = map(int, input().split())# tort = []# for i in range(r):#     tort.append(input())## mas = [[False]*c for i in range(r)]# for i in range(r):#     if 'S' not in tort[i]:#         for j in range(c):#             mas[i][j] = True# for j in range(c):#     is_find = False#     for i in range(r):#         if tort[i][j] == 'S':#             is_find = True#             break#     if not is_find:#         for i in range(r):#             mas[i][j] = True# count = 0# for row in mas:#     count += row.count(True)# print(count)### zeroes = [i*0 for i in range(100)]# print([i for i in range(1, int(input())+1)])### n = int(input())# print([i for i in range(1,n+1) if n % i == 0])## print((lambda n: [i for i in range(1, n + 1) if n % i == 0])(int(input())))## n = int(input())# print([i for i in range(n,n**2+1) if i % 2 != 0])### a, b = map(int, input().split())# if a <= b:#     print([i**2 for i in range(a,b+1)])# else:#     print([i**3 for i in range(a, b-1, -1)])## st = 'Create a list of the first letters of every word in this string'# print([i[0] for i in st.split()])### from string import ascii_uppercase# n = int(input())# s = [i for i in ascii_uppercase]# print(s[:n])## print([ascii_uppercase[i] for i in range(int(input()))])## print([i for i in ascii_uppercase[0:int(input())]])## from string import ascii_uppercase# print([ascii_uppercase[i-1]*i for i in range(1,int(input())+1)])## print([chr(i)*(i-64) for i in range(65, int(input())+65)])### phrase = 'Take only the words that start with t in this sentence'# print([i for i in phrase.split() if i[0] == 't' or i[0] == 'T'])### phrase = 'Take only the words that start with t in this sentence'# print([w for w in phrase.split() if w.startswith(('t', 'T'))])# print(tuple(range(2, 6)))## n = int(input())# if n % 2 == 1:#     print(tuple(range(n,n**2+1,2)))# else:#     print(tuple(range(n+1,n**2+1,2)))# n = int(input())# triangle = []# for i in range(n + 1):#     triangle.append([1] + [0] * n)## for i in range(1, n + 1):#     for j in range(1, n + 1):#         triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]## for i in range(0, n + 1):#     for j in range(0, n + 1):#         print(triangle[i][j], end='')#     print()# days = {#     1: 31,#     2: 28,#     3: 31,#     4: 30,#     5: 31,#     6: 30,#     7: 31,#     8: 31,#     9: 30,#     10: 31,#     11: 30,#     12: 31# }# print(days[int(input())])### from string import ascii_lowercase# alphabet = {i: j for i, j in zip(ascii_lowercase, range(1,27))}# print(alphabet)# a = {1: "one", 2: "two"}# b = {2: "dva", 3: "three"}# c = {3: "tri", 2: "два"}## result = c | a | b# print(result[2])# logins = {}# for i in range(int(input())):#     login = input()#     if login in logins:#         print(f'{login}{logins[login]}')#         logins[login] += 1#     else:#         print('OK')#         logins[login] = 1## countries = {#     "Sweden": ["Stockholm", "Göteborg", "Malmö"],#     "Norway": ["Oslo", "Bergen", "Trondheim"],#     "England": ["London", "Birmingham", "Manchester"],#     "Germany": ["Berlin", "Hamburg", "Munich"],#     "France": ["Paris", "Marseille", "Toulouse"]# }## city = input()# for key,value in countries.items():#     if city in value:#         print(f"INFO: {city} is a city in {key}")#         break# else:#     print(f'ERROR: Country for {city} not found')## user = {#     "id": 4170,#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",#     "password": "SyUpfo1ljm",#     "first_name": "Teresa",#     "last_name": "Wehner",#     "username": "teresa.wehner",#     "email": "teresa.wehner@email.com",#     "gender": "Non-binary",#     "phone_number": "+674 424.561.2776",#     "social_insurance_number": "637316241",#     "date_of_birth": "1993-08-17"# }# user['secret'] = user.pop("password")# user['surname'] =  user.pop("last_name")# print(user)# tot = [int(i) for i in input().split()]# res = tot[-1]# for i in reversed(range(len(tot) - 1)):#     res = {tot[i]: res}# print(res)# workers = {#     'employer1': {'name': 'Jhon', 'salary': 7500},#     'employer2': {'name': 'Emma', 'salary': 8000},#     'employer3': {'name': 'Brad', 'salary': 500}# }# workers['employer3']['salary'] = 8500# print(workers)## s = input().lower()# catalog = {}# for i in s:#     if i.isalpha():#         catalog[i] = catalog.get(i,0) + 1# print(catalog)# summ = 0# supermarket = {#     "milk": {"quantity": 20, "price": 1.19},#     "biscuits": {"quantity": 32, "price": 1.45},#     "butter": {"quantity": 20, "price": 2.29},#     "cheese": {"quantity": 15, "price": 1.90},#     "bread": {"quantity": 15, "price": 2.59},#     "cookies": {"quantity": 20, "price": 4.99},#     "yogurt": {"quantity": 18, "price": 3.65},#     "apples": {"quantity": 35, "price": 3.15},#     "oranges": {"quantity": 40, "price": 0.99},#     "bananas": {"quantity": 23, "price": 1.29}# }# for i in supermarket:#     summ += supermarket[i]["quantity"] * supermarket[i]["price"]## print(summ)# print('YES' if sorted(input()) == sorted(input()) else 'NO')## s1,s2 = input(), input()# d1 = {i: s1.count(i) for i in s1}# d2 = {i: s2.count(i) for i in s2}# print('YES' if d1 == d2 else 'NO')## morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',#          'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',#          'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',#          'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',#          'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',#          'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',#          'y': '—•——', 'z': '——••'}# s = [i for i in input().lower().split()]# for i in s:#     for j in i:#         print(morze[j]+' ',end='')#     print()### print(*('\n' if i == ' ' else morze[i] + ' ' for i in input().lower()), sep='')## [print(*[morze[i] for i in _]) for _ in input().lower().split()]## for i in input().lower().split():#     print(*[morze[j] for j in i])# persons= [#     ('Allison Hill', 334053, 'M', '1635644202'),#     ('Megan Mcclain', 191161, 'F', '2101101595'),#     ('Brandon Hall', 731262, 'M', '6054749119'),#     ('Michelle Miles', 539898, 'M', '1355368461'),#     ('Donald Booth', 895667, 'M', '7736670978'),#     ('Gina Moore', 900581, 'F', '7018476624'),#     ('James Howard', 460663, 'F', '5461900982'),#     ('Monica Herrera', 496922, 'M', '2955495768'),#     ('Sandra Montgomery', 479201, 'M', '5111859731'),#     ('Amber Perez', 403445, 'M', '0602870126')# ]## data = {}# for i in persons:#     name = i[0]#     salary = i[1]#     gender = i[2]#     passport = i[3]#     data[name] = {'salary': salary, 'gender': gender, 'passport':passport}## print(data)# data = {#     "my_friends": {#         "count": 10,#         "people": [{#             "first_name": "Kurt",#             "id": 621547005,#             "last_name": "Cobain",#             "bdate": "31.8.2005"#         }, {#             "first_name": "Виолетта",#             "id": 484200150,#             "last_name": "Кастилио",#         }, {#             "first_name": "Иринка",#             "id": 21886133,#             "last_name": "Бушуева",#             "bdate": "28.8.1942"#         }, {#             "first_name": "Данил",#             "id": 282456573,#             "last_name": "Греков",#             "bdate": "4.7.2002"#         }, {#             "first_name": "Валентин",#             "id": 184902932,#             "last_name": "Долматов",#             "bdate": "25.5"#         }, {#             "first_name": "Евгений",#             "id": 620469646,#             "last_name": "Шапорин",#             "bdate": "6.12.1982"#         }, {#             "first_name": "Ангелина",#             "id": 622328862,#             "last_name": "Краснова",#             "bdate": "4.11.1995"#         }, {#             "first_name": "Иван",#             "id": 576015198,#             "last_name": "Вирин",#             "bdate": "2.2.1915"#         }, {#             "first_name": "Паша",#             "id": 386922406,#             "last_name": "Воронов",#             "bdate": "27.9"#         }, {#             "first_name": "Ольга",#             "id": 622170942,#             "last_name": "Савченкова",#             "bdate": "20.12"#         }]#     }# }# a = []# for i in data["my_friends"]['people']:#     for j in data["my_friends"]['people']:#         if j['first_name'] not in a:#             a.append(j['first_name'])# a.sort()# print(a)# user = {#     "id": 4170,#     "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",#     "password": "SyUpfo1ljm",#     "first_name": "Teresa",#     "last_name": "Wehner",#     "username": "teresa.wehner",#     "email": "teresa.wehner@email.com",#     "gender": "Non-binary",#     "phone_number": "+674 424.561.2776",#     "social_insurance_number": "637316241",#     "date_of_birth": "1993-08-17",#     "employment": {#         "title": "Central Hospitality Liaison",#         "key_skill": "Organisation"#     },#     "subscription": {#         "plan": "Essential",#         "status": "Idle",#         "payment_method": "Debit card",#         "term": "Annual"#     }# }# print({i:user[i] for i in input().split()})# vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]# print([i for j in vector for i in j])### from string import ascii_lowercase## text =  set(input().lower())# if text == set(ascii_lowercase):#     print('YES')# else:#     print('NO')### print(len(set(input()) - set('{ },')))## print(len(set(input()[1:-1:3])))## print(sum(i.isalpha() for i in set(input())))# words = ['mention', 'soup', 'pneumonia', 'tradition', 'concert', 'tease', 'generation',#          'winter', 'national', 'jacket', 'winter', 'wrestle', 'proposal', 'error',#          'pneumonia', 'concert', 'value', 'value', 'disclose', 'glasses', 'tank',#          'national', 'soup', 'feel', 'few', 'concert', 'wrestle', 'proposal', 'soup',#          'sail', 'brown', 'service', 'proposal', 'winter', 'jacket', 'mention', 'tradition',#          'value', 'feel', 'bear', 'few', 'value', 'winter', 'proposal', 'government',#          'control', 'value', 'few', 'generation', 'service', 'national',#          'tradition', 'government', 'mention', 'proposal']# set_ = set([i for i in words if len(i) > 6])# print(len(set_))#### cat = [[int(i) for i in input().split()] for i in range(int(input()))]# for i in cat:#     print(len(set(i)))### for _ in range(int(input())):#     print(len(set(input().split())))### [print(sum(len(set(input().split()))) for _ in range(int(input())))]## print(*(len(set(input().split())) for i in range(int(input()))), sep='\n')# cat = [i.lower() for i in input().split(',')]# s = set()# for i in cat:#     if i not in s:#         print('НЕТ')#         s.add(i)#     else:#         print('ДА')s = input()cat = set()for i in range(len(s)):    if s[i].isdigit() and s.count(s[i]) > 1:        cat.add(s[i])if len(cat) > 0:    print(*sorted(cat))else:    print('NO')str = input()c = set()for i in str:  if i.isdigit() and str.count(i) > 1:    c.add(i)print (*sorted(c) if c else ["NO"])