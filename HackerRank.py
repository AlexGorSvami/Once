#                                   First:
# def is_leap(year):
#     leap = False
#
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         leap = True
#
#     return leap
#
#
# year = int(input())

                        # Twice:

# if __name__ == '__main__':
#     n = int(input())
#     answer = "1"
#     for i in range(2, n + 1):
#         answer += str(i)
#
# print(int(answer))

                        # Third

# a,b,m = int(input()),int(input()),int(input())
#
# print(pow(a,b))
# print(pow(a,b,m))

                        # Fouth:

# a,b,c,d = int(input()),int(input()),int(input()),int(input())
#
# print(pow(a,b) + pow(c,d))

                        # Fifth:

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
# l = []
# for i in range (x +1):
#     for j in range(y + 1):
#         for k in range (z + 1):
#             if i + j + k != n:
#                 l.append([i,j,k])
# print(l)

#
# print([[i,j,k] for i in range(x + 1) for j in range (y + 1) for k in range (z + 1) if i+j+k != n])

arr = [5,2,3,4,5]

arr.sort()
print(arr)
print(arr[arr.index(max(arr))-1])
