# # # from encodings.aliases import aliases
# # #
# # # original=[1,2,3]
# # # alias=original
# # # alias.append(4)
# # # print(original)
# #
# #
# # original=[1,2,3,]
# # clone1=original[:]
# # clone2=original.copy()
# # clone1.append(4)
# # clone2.append(8)
# # print(original)
# # print(clone1)
# # print(clone2)
#
# lst=[3,1,2,1,5]
# print("original list:",lst)
#
# lst.append(5)
# print(lst)
#
#
# name="java"
# for index, character in enumerate(name):
#     print(index,character)

even_numbers=[i for i in range(1,11)if i%2==0]
print(even_numbers)