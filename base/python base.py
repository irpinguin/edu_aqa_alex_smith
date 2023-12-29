# #
# seq = [i for i in range(10)]
# print(seq)
# print(f'[0:5]: {seq[0:5]}')
# print(f'[-5:-1]: {seq[-5:-1]}')
# print(f'[-5:]: {seq[-5:]}')
# print(list(range(10)))

# #
# print()
# i = 0
# my_lst = ["elem_1", "elem_2", "elem_3", "non_elem"]
#
# while i != (len(my_lst)-1):
#     print(my_lst[i])
#     i += 1
# print()
# for item in my_lst:
#     print(item)

# # list
# family_lst = ["Alex", "Olga", "Nasty", "Alex"]
# print(family_lst)
# # set
# family_set = {"Alex", "Olga", "Nasty", "Alex"}
# print(family_set)
# dictionary
# family_dict = {"user":"Alex", "admin":"Olga", "developer":"Nasty", "tester":"alex"}
# # print(family_dict["admin"])
#
# for key, val in family_dict.items():
#     print(key + " - " + val)

# files
# buf = input("Type your text here...")
# fw = open('./doc/file.txt', 'a')
# fw.write(buf)
# fw.close()

# fw = open('./doc/file.txt', 'w')
# fw.write("overwrite")
# fw.close()

# with open('./doc/file_2.txt', 'w') as fr:
#     fr.write("Content\n")
#
# with open("./doc/file_2.txt", "r+") as fr:
#     content = fr.read()
#     print(f'1 step: file contains\n{content}')
#     fr.write("New content\n")
#
# with open("./doc/file_2.txt", "r") as fr:
#     content = fr.read()
#     print(f'2 step: file contains\n{content}')
#
# fr.close()

# modules

# exception
