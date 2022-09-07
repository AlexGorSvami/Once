# n = int(input())
# h = (n // 60) % 24
# print(h, n % 60)
#
# num = int(input())
# end ='.'
# print('The next number for the number', str(num), 'is', str(num+1)+'.')
# print ('The previous number for the number', str(num), 'is', str(num-1)+'.')

# a,b,c = int(input()),int(input()),int(input())
# print((a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2))
#
# a,b,l,N = int(input()),int(input()),int(input()),int(input())
# print(2*l+(2*N-1)*a+2*(N-1)*b)

# a,b,c,d = int(input()),int(input()),int(input()),int(input())
# if (a+b) % 2 == 0 and (c+d) % 2 == 0 or (a+b) % 2 != 0 and (c+d) % 2 != 0:
#     print('YES')
# else:
#     print('NO')

# my_str = 'Valera'
#
# new_str = my_str[len(my_str)//2-1:len(my_str)//2+1]
#
# print(new_str)


# def end_zeros(a: int) -> int:
#     zer = 0
#     a = str(a)
#     for i in a[::-1]:
#         if int(i) == 0:
#             zer += 1
#         else:
#             break
#     return zer
#
# print(end_zeros(1000))
#
# def end_zeros(number):
#     n = str(number)
#     return len(n) - len(n.strip('0'))
#
# def end_zeros(number):
#     number = str(number)
#     if number[-1:] != '0':
#         return 0
#     return 1 + end_zeros(number[:-1])


# def index_power(list_, number) -> int:
#     if number > len(list_):
#         return -1
#     else:
#         return list_.pop(number) ** number
#
# print(index_power([1,2,3], 2))

# def between_markers(text: str, start: str, end: str) -> str:
#     s = text.find(start)
#     l = text.find(end)
#     return text[s:l:].strip(start)
#
# print('Example:')
# print(between_markers('What is >apple<', '>', '<'))

def replace_first(items: list):
    if len(items) == 0 or len(items) == 1:
        return items
    else:






