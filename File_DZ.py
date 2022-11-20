#
# from pprint import pprint
#
#
# def create_cook_book():
#     cook_book = {}
#     with open('Recipes.txt') as file:
#         for line in file:
#             dish = line.strip()
#             count = int(file.readline())
#             ingredients_list = []
#             for item in range(count):
#                 ingredients = {}
#                 ingredient = file.readline().strip()
#                 ingredients['ingredient_name'], ingredients['quantity'], ingredients['measure'] = ingredient.split('|')
#                 ingredients['quantity'] = int(ingredients['quantity'])
#                 ingredients_list.append(ingredients)
#             file.readline()
#             cook_book[dish] = ingredients_list
#     return cook_book
#
#
# if __name__ == '__main__':
#     filename = "Recipes.txt"
#     cook_book = create_cook_book()
# print(cook_book)
#
# def get_shop_list_by_dishes(dishes, persons):
#     ing_list = dict()
#     for dish_name in dishes:
#         if dish_name in cook_book:
#             for ing in cook_book[dish_name]:
#                 measure_list = dict()
#                 if ing['ingredient_name'] not in ing_list:
#                     measure_list['measure'] = ing['measure']
#                     measure_list['quantity'] = ing['quantity'] * persons
#                     ing_list[ing['ingredient_name']] = measure_list
#                 else:
#                     ing_list[ing['ingredient_name']]['quantity'] = ing_list[ing['ingredient_name']]['quantity'] + \
#                                                                      ing['quantity'] * persons
#         else:
#             print('Ошибка! Такого блюда не существует')
#     return ing_list
#
# pprint(get_shop_list_by_dishes(dishes=['Омлет', 'Омлет'], persons=2))
#
#
# def rwrite_file(file_1, file_2, file_3):
#         with open(file_1) as f1:
#             file1 = f1.readlines()
#         with open(file_2) as f2:
#             file2 = f2.readlines()
#         with open(file_3) as f3:
#             file3 = f3.readlines()
#         with open('final.txt', 'w') as f_total:
#
#             if len(file1) < len(file2) and len(file1) < len(file3):
#                 f_total.write(file_1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#                 f_total.write('\n')
#             elif len(file2) < len(file1) and len(file2) < len(file3):
#                 f_total.write(file_2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#                 f_total.write('\n')
#             elif len(file3) < len(file1) and len(file3) < len(file2):
#                 f_total.write(file_3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#                 f_total.write('\n')
#             if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
#                 f_total.write(file_1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#                 f_total.write('\n')
#             elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
#                 f_total.write(file_2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#                 f_total.write('\n')
#             elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
#                 f_total.write(file_3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#                 f_total.write('\n')
#             if len(file1) > len(file2) and len(file1) > len(file3):
#                 f_total.write(file_1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#             elif len(file2) > len(file1) and len(file2) > len(file3):
#                 f_total.write(file_2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#             elif len(file3) > len(file1) and len(file3) > len(file2):
#                 f_total.write(file_3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#         return
#
#
# write_file('1.txt','2.txt','3.txt')




