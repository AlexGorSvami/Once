# f = open('/home/alex/Рабочий стол/Синтаксис генератора списков: [ element for variable(s) in list if condition ]')# print(type(f))## # прочитываеn всё содержимое файла в одной строке# content = f.read()# f.seek(0)# content2 = f.read()# print(type(content))# print(content2)# прочитывает одну строку:# line = f.readline()# line2 = f.readline()# line3 = f.readline()# print(line3)# from pprint import pprint# # прочитывет все строки в виде списка:# content = f.readlines()# print(type(content))# pprint(content)# with open ('/home/alex/Рабочий стол/Синтаксис генератора списков: [ element for variable(s) in list if condition ]') as f:#     content = f.readlines()#     print(content[2])# with open('/home/alex/Рабочий стол/Синтаксис генератора списков: [ element for variable(s) in list if condition ]', 'rt') as f:#     content = f.readlines()#     for line in content:#         data = line.split(' ')#         print(data)# with open('test.txt', 'rt') as f:#     result = []#     for line in f:#         data = line.split(' | ')#         result.append({'name' : data[0],#                                 'stock': data[1],#                                 'price': int(data[2])})#     print(result)# запись:# w (write) - перещапись (стирает содержимое файла)# a (append) -  дозапись (записывает в конец файла)# x (exclusive) - запись (только в новый файл)# with open('test2.txt', 'x') as file:#     # file.write('World\n')#     # file.write('Hello\n')#     file.writelines(['String1\n', 'String2\n'])# with open ('test1.txt', 'a+') as file:#     file.seek(0)#     content = file.read()#     print(content)#     file.write('String 3')# with open('test2.txt', 'w+') as file:#     file.write("Hello Ben")#     file.seek(0)#     content = file.read()#     print(content)# with open('test.txt', 'a') as file:#     print(file.readable())#     print(file.writable())## with open('folder1/file1.txt', 'r') as file:#     content = file.read()#     print(content)## with open('/home/alex/PycharmProjects/pythonProject/folder1/file1.txt', 'r') as file:#     content = file.read()#     print(content)# import os## BASE_DIR = os.getcwd()# FOLDER_NAME = 'folder1'# FILE_NAME = 'file1.txt'## # full_path = f'{BASE_DIR}/{FOLDER_NAME}/{FILE_NAME}'# full_path = os.path.join(BASE_DIR, FOLDER_NAME, FILE_NAME)# print(full_path)## with open(full_path, 'r') as f:#     content = f.read()#     print(content)# f = open('data.txt', encoding="UTF-8")# print(type(f))# прочитывает всё содержимое в виде одной большой строки (str)# content = f.read()# f.seek(0)# ставит указатель в начало файла# content2 = f.read()# print(type(content))# print(content)# print(type(content2))# print(content2)# f.close()# прочитывает только одну строку# line = f.readline()# line2 = f.readline()# line3 = f.readline()# line4 = f.readline()# print(line)# print(line2)# print(line4)# from pprint import pprint# # прочитывает все строки в виде спискa# content = f.readlines()# print(type(content))# pprint(content)# with open('data.txt', encoding='utf-8') as f:#     print(type(f))#     content = f.readlines()#     print(content[1])# from pprint import pprint# with open('data.txt', 'r', encoding='utf-8') as f:#     result = []#     for line in f:#         data = line.split('|')#         result.append({'name': data[0],#                        'stock': data[1],#                        'price': data[2]})#     pprint(result)# запись# w(write) - перезапсь (стирает содержимое файла)# a (append) - дозапись в конец файла# x (exclusive) - запись (записывает только в новый файл)# with open('text.txt', 'w', encoding='utf-8') as f:#     # f.write('Hello\n')#     # f.write('World\n')#     f.writelines(['String 1\n', 'String 2\n'])# with open('text.txt', 'a', encoding='utf-8') as f:#     f.writelines(['String 3\n', 'String 4\n'])# with open('text2.txt', 'x', encoding='utf-8') as f:#     f.writelines(['String 3\n', 'String 4\n'])# with open('text.txt', 'a+', encoding='utf-8') as file:#     file.seek(0)#     content = file.read()#     file.write('String 14\n')#     print(content)# with open('test2.txt', 'w+', encoding='utf-8') as file:#     file.write('Hello World!')#     file.seek(0)#     content = file.read()#     print(content)# + позволяет дополнительно к записи читать файл# Возможные ошибки:# - открытие несуществующего файла# - открытие файла в неправильном режиме# # - методы readable и writable возвращают True,False с их помощью можно проверить текущий режим# with open('folder1/file1.txt', 'r') as file:#     content = file.read()#     print(content)import osBASE_DIR = os.getcwd()FOLDER_NAME = 'folder1'FILE_NAME = 'file1.txt'# full_path = f'{BASE_DIR}/{FOLDER_NAME}/{FILE_NAME}'full_path = os.path.join(BASE_DIR, FOLDER_NAME, FILE_NAME)print(full_path)with open(full_path) as f:    content = f.read()    print(content)# def exc(text):#     assert text != ''#     print(str(text) + '!')## exc('Hello World')## def test(number):#     assert number > 0, 'Число меньше нуля!!!!'#     print(str(number))## test(-10)# # test(10)# filename = input('Введите желаемое имя файла')# text = input('Какой текст хотите поместить в файл')# file = open(filename, 'w')## file.write(text)## file.close()# file = open('text.txt', 'r')## print(file.read())## file.close()# with open('test.txt') as f1:#     with open ('text1.txt', 'w') as f2:#         f2.write(f1.read())# просмотр кода символа:# print(ord('r'))# print(chr(100))# for ch in 'hello':#     print(ord(ch))## codes = [104, 101, 108, 108, 111]# # собираем строку обратно# out = ''# for code in codes:#     out += chr(code)# print(out)# какие символы вообще есть?# for code in range(128):#     print(code, hex(code), chr(code))# получилась таблица символов ASCII# то есть каждый символ имеет свой кодю В пайтоне символы храяняться в кодах unicode# http://foxtools.ru/Unicode# Эта таблица стандарт для ВСЕХ символов, которое придумало человечество# Это именно стандарт а не кодировка - сам по себе Юникод не определяет,# как символы будут хранится на жестком диске или передаваться по сети.# Он лишь определяет связь, между символом и некоторым числом# for code in range(1000, 1200):#     print(code, chr(code))# но коды символов больших чем байт (256) будут занимать несколько байтю# Поэтому есть форматы представления текста - как ханить коды юникода.# например старший байт из двух/трех/етс идет первым или вторым?## наиболее распространенным является представление UTF-8 - http://ru.wikipedia.org/wiki/UTF-8# и в реальности на дисках наши тексты сохраняются в одном из форматов предсьавления## Как хранить не строки, но сами байты?# В пайтоне есть тип данных, который позволяет хранить "сырые байты" - bytes# bb = b'\xd1\x84'# print(bb)# Тип bytes очень похож на str# bb = b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'# print(bb)# print(type(bb))# # по сути это неизменяемые последовательности целых чисел,# # поддерживают те же операции что и str# print(bb[0])# print(bb.count(0xd0))# print(b'he' + b'llo')# bb = b'\xd1\x84'# print(bin(0xd1))# print(bin(0x84))## code = 0b10001000100# print(code, hex(code))# print(chr(code))# ba = bytearray(b'hello')# ba[0] = 32 #код пробeла# print(ba)# print(bytearray())# print(bytearray(16))# print(bytearray(range(16)))# print(bytearray(b'hello'))# print(bytearray('привет', encoding='utf-8'))# print(bytearray('привет'.encode(encoding='utf-8')))### # для преобразования байтов в строку и обратно есть две функции## # строка а байты# print('привет'.encode(encoding='utf-8'))# print('привет'.encode(encoding='utf-16'))# print('привет'.encode(encoding='cp866'))# # то есть мы хотим ЗАКОДИРОВАТЬ коды уникода в нужное представлене## # байты в строку# ss = b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'.decode(encoding='utf-8')# print(ss)import io# f = 'test.txt'# file = open(f)# content = file.read(100)# print(content)## new_pos = file.seek(11, io.SEEK_SET)# # io.SEEK_SET - начало файла# # io.SEEK_CUR - текущая позиция# # io.SEEK_END - конец файла## content = file.read(100) #в символах# print(content)## file.close()# f = 'test.txt'# file = open(f)# from pprint import pprint## pprint(file.name)# pprint(file.mode)# pprint(file.encoding)# pprint(file.closed)## pprint(file.readable())  # файл можно читать# pprint(file.writable())  # файл можно записывать# pprint(file.seekable())  # поддерживает произвольный доступ## pprint(file.truncate(size=None))# pprint(file.flush())  # обычно фай л буфферизован, флаш записывает весь буфер на диск# файлы по сути являются потоками байтов - streamsf = 'test.txt'file = open(f)# for line in file: # если файл огромный - будет читать только строку#     print(line, end='')# file.close()# lines = file.readlines()# for line in lines:#     print(line, end='')# file.close()# line = True# while line:#     line = file.readline()#     if 'Apple' in line:#         print('Yes')#         break# else:#     print('NO')# file.close()# with open(f, 'r' ) as file:#     for line in file:#         print(line)# print(file.closed)# with работает с контекстными менеджерами# class InOutBlock:##     def __enter__(self):#         print('In block code')##     def __exit__(self, exc_type, exc_val, exc_tb):#         print('Out in block code')## with InOutBlock() as in_out:#     print('Incorrect code')# то еесть объект файла реализует интерфейс контекстного менеджера# и закрывает файл кода