# word = input()
# print('YES' if word == word[::-1] else 'NO')

# s = 'efgabcd'
# print(s[(len(s) + 1) // 2:] + s[:(len(s)+1) // 2])
# print(s[-(len(s)//-2):]+s[:-(len(s)//-2)])

# print('YES' if (s := input()) == s.title() else 'NO')
#
# print('YES' if 'хорош' in input().lower() else 'NO')
#
# print(sum(s.islower() for s in input()))
#
# n = int(input())
# count = 0
# while n > 0:
#     s = input()
#     if s.count('11') >= 3:
#         count += 1
#     n -= 1
# print(count)
#
# print(sum(input().count('11') > 2 for _ in range(int(input()))))
#
# n = input()
# count = 0
# for i in range(10):
#     count += n.count(str(i))
# print(count)
#
# s = input()
# print('YES' if s.endswith('.com') or s.endswith('.ru') else 'NO')
#
# s = 'aaaaabbbbbccc'
# dictionary = {symbol: s.count(symbol) for symbol in s}
# print(dictionary[max(dictionary, key=dictionary.get)])
# print(max(dictionary, key=dictionary.get))


# s = 'aaaaabbbbbccc'
# a = 0
# fin = ''
# for i in range(len(s)):
#     if s.count(s[i]) >= a:
#         fin = s[i]
# print(fin)
#
# s = 'aaaaabbbbbccc'
# max = 0
# b = 0
# for i in s:
#     if s.count(i) >= max:
#         max = s.count(i)
#         b = i
# print(b)

a = input()[::-1]
z = max(a, key = a.count)
print(z)


s = input()
if s.count('f') > 1:
    print(s.find('f'),s.rfind('f'))
elif s.count('f') == 1:
    print(s.find('f'))
else:
    print('NO')

text = input()
print(text[:text.find("h")] + text[text.rfind("h") + 1:])

print(*[chr(i) for i in range(int(input()), int(input())+1)])

cod = int(input())
s = input()
for i in s:
    dec = ord(i)-cod
    if dec < 97:
        dec += 26
    print(chr(dec), end='')


n = int(input())
s = input()
res = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(s)):
    res += alphabet[alphabet.find(s[i])-n]
print(res)