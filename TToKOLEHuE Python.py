# word = input()
# print('YES' if word == word[::-1] else 'NO')

s = 'efgabcd'
print(s[(len(s) + 1) // 2:] + s[:(len(s)+1) // 2])
print(s[-(len(s)//-2):]+s[:-(len(s)//-2)])