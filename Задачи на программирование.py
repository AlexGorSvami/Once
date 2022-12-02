n = int(input())
# count = 0
# for i in range(1, n + 1):
#     for j in range(i):
#         count += 1
#         if count > n:
#             break
#         print(i, end=' ')

result = [i for i in range(1, n+1) for _ in range(i)][:n]
[print(i, end=' ') for i in result]



