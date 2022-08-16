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

a = [0] * 5
print(a)
a = [0 for i in range(5)]
print(a)
a = [i * i for i in range(5)]
print(a)
a = [int(i) for i in input().split()]
print(a)