# def first_word(str):
#     for i in str:
#         print(i, end='')
#         if i == ' ':
#             break
#
#
# assert first_word("Hello world") == "Hello"
# assert first_word("a word") == "a"
# assert first_word("greeting from CheckiO Planet") == "greeting"
# assert first_word("hi") == "hi"
#
#
#
# def first_word(text: str) -> str:
#     return text.replace(".", " ").replace(",", " ").split()[0]

students = ['Ivan', 'Masha', 'Sasha']
# for student in students:
#     print(f'Hello {student}!')
#
# print(len(students))
# print(students[0])
# print(students[-1])
# print(students[::-1])
# teachers = ['Vova', 'Lox']
#
# print(students + teachers)
#
# students[1] = 'Oleg'
# print(students)
# students.append('Olga')
# print(students)
# students +=['Olga']
# print(students)
# students.insert(1, 'Dal')
# print(students)

# students.remove('Sasha')
# print(students)
# del students[0]
# print(students)

# ind = students.index('Sasha')
# print(ind)
# oed_stud = sorted(students)
# print(oed_stud)
# students.sort()
# print(min(students))


# a = [1, 'A', 2]
# b = a
# a[0] = 42
# print(a)
# print(b)
# b[2] = 30
# print(b)
# print(a)
#
# a = [int(i) for i in input().split()]
# print(a[::2])


# chet = []
# a = [int(i) for i in input().split()]
# for i in a:
#     if i % 2 == 0:
#         chet.append(i)
# print(*chet)


# s = [int(i) for i in input().split()]
# count = 0
# for i in range(1, len(s) - 1):
#     if s[i] > s[i-1] and s[i] > s[i + 1]:
#         # or s[i-1] < s[i] > s[i+1]:
#         count += 1
#
# print(count)


# s = [int(i) for i in input().split()]
# print(max(s), s.index(max(s)))


s = [int(i) for i in input().split()]
x = int(input())
s.append(x)
s.sort()
print(s.index(x))