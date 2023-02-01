# Задача Иосифа Флавия 🌶️🌶️
#
# nn человек, пронумерованных числами от 11 до nn, стоят в кругу. Они начинают считаться, каждый kk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер человека, который останется в кругу последним.
#
# Формат входных данных
# На вход программе подаются два числа nn и kk, записанные на отдельных строках.
#
# Формат выходных данных
# Программа должна вывести одно число – номер человека, который останется в кругу последним.

# n,k = int(input()),int(input())
# l = 0
# for i in range(1,n+1):
#     l = (l + k) % i
# print(l +  1)

# ------------------------------------------------------------------------------------------------------------------
#                                                     Координатные четверти
# Формат входных данных
# В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел — координат точки (сначала абсцисса – xx, затем ордината – yy), разделенных символом пробела.

# mas = [[int(i) for i in input().split()] for i in range(int(input()))]
# first = 0
# second = 0
# third = 0
# fourth = 0
# for i in mas:
#     if i[0]  ==   0 or i[1] == 0:
#         continue
#     if i[0] > 0:
#         if i[1] > 0:
#             first += 1
#         else:
#             fourth += 1
#     else:
#         if i[1] > 0:
#             second += 1
#         else:
#             third += 1
#
# print(f'''Первая четверть: {first}
# Вторая четверть: {second}
# Третья четверть: {third}
# Четвертая четверть: {fourth}''')
#
#
#
# n = int(input())
# count = [0, 0, 0, 0]
# names = ['Первая четверть:', 'Вторая четверть:',
#          'Третья четверть:', 'Четвертая четверть:']
#
# for _ in range(n):
#     x, y = [int(num) for num in input().split()]
#     if x > 0 and y > 0:
#         count[0] += 1
#     elif x < 0 and y > 0:
#         count[1] += 1
#     elif x < 0 and y < 0:
#         count[2] += 1
#     elif x > 0 and y < 0:
#         count[3] += 1
#
# for i in range(4):
#     print(names[i], count[i])
#
#
# a = [tuple(map(int, input().split())) for n in range(int(input()))]
# print('Первая четверть: {}'.format(sum([1 for t in a if t[0] > 0 and t[1] > 0])))
# print('Вторая четверть: {}'.format(sum([1 for t in a if t[0] < 0 and t[1] > 0])))
# print('Третья четверть: {}'.format(sum([1 for t in a if t[0] < 0 and t[1] < 0])))
# print('Четвертая четверть: {}'.format(sum([1 for t in a if t[0] > 0 and t[1] < 0])))

# ---------------------------------------------------------------------------------------------------------------------
# На вход программе подается строка текста из натуральных чисел.Из элементов строки формируется список чисел.Напишите программу, которая меняет местами соседние элементы
# списка(a[0] c a[1], a[2] c a[3] и т.д.).Если в списке нечетное количество элементов, то последний остается на своем месте.

# mas = [int(i) for i in input().split()]
# if len(mas) == 1:
#     mas = mas
# elif len(mas) %  2 ==  0:
#     for i in range(0,len(mas),2):
#         mas[i],mas[i+1]  = mas[i+1],mas[i]
# else:
#     for i in range(0,len(mas)-1,2):
#         mas[i],mas[i+1]  = mas[i+1],mas[i]
#
# print(*mas)
#
#
#
# digits = [int(c) for c in input().split()]
#
# for i in range(1, len(digits), 2):
#     digits[i - 1], digits[i] = digits[i], digits[i - 1]
#
# print(*digits)

# ----------------------------------------------------------------------------------------------------
# n = int(input())
# flag = 'НЕТ'
# mas = [int(i) for i in input().split()]
# for k in mas:
#     big = k
#     for i in range(n + 1):
#         for j in range(n + 1):
#             if big == mas[i] * mas[j]:
#                 flag = 'ДА'
#                 break
#
# print(flag)

# --------------------------------------------------------------
#                     Камень, ножницы, бумага

# x, y = input(), input()
# var = ['камень', 'ножницы', 'бумага']
# ans = ['ничья', 'Руслан', 'Тимур']
# print(ans[var.index(x) - var.index(y)])
#
# print(['ничья', 'Тимур', 'Руслан'][input().count('а') - input().count('а')])





# s = input().split('О')
# print(len(max(s)))

# n = int(input())
# mas  = [[j for j in input()] for i in range(n)]
# for i in range(len(mas)):
#     if 'a' in mas[i] and mas[i].count('n') >= 2 and 't' in mas[i] and 'o' in mas[i] :
#         print(i+1, end=' ')


# mas = [float(i) for i in input().split()]
# for i, el in enumerate(mas):
#     if  el < 0:
#         mas[i] = -1.0
#
# print(mas)

mas = [int(input()) for i in range(int(input()))]
num = int(input())
flag = 'НЕТ'
for i in range(len(mas) ):
    for j in range(len(mas) ):
        if i != j:
            if mas[j] * mas[i] == num:
                flag = 'ДА'

print(flag)