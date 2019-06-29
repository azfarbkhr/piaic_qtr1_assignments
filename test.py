# length = 4



# # logic for following triangle
# #          *
# #         ***
# #        *****
# #       *******
# #      *********
# #     ***********
# #    *************
# #   ***************
# #  *****************
# # *******************

# # for i in range(length):
# #     for j in range(length - 1, i, -1):
# #         print(" ", end = "")
# #     for k in range((2 * i) + 1):
# #         print("*", end = "")
# #     for j in range(length - 1, i, -1):
# #         print(" ", end = "")
# #     print("")

# # _____________________________________________________________________________________________________________________

# # logic for following triangle
# # *
# # * *
# # * * *
# # * * * *
# # * * *
# # * *
# # *

# # for i in range(length):
# #     for j in range(i + 1):
# #         print("*", end = " ")
# #     print("")
# # for i in range(length - 1):
# #     for j in range(length - i -1):
# #         print("*", end = " ")
# #     print("")


# # ________________________________________________________________________________________________________
# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *

# for i in range(5):
#     for j in range(5-i-1):
#         print(" ", end = " ")
#     for k in range(i + 1):
#         print("*", end = " ")
#     print("")



###### how to create a new class and its methods
# class Human():
#     def __init__(self, name, father_name='', favourite_dish = 'Biryani'):
#         self.name = name
#         self.father_name = father_name
#         self.favourite_dish = favourite_dish
#         print('inside constructor')
    
#     def eat(self):
#         print(self.favourite_dish, 'ley ao!')


# azfar = Human('Syed Azfar ALi', 'Laiq Ali', 'Pizza')

# # print(azfar.name, "like to eat", azfar.favourite_dish)
# azfar.eat()

#### file open
# with open("file.txt", "w") as f:
#     f.write('write a line')

# with open("file.txt", "r") as f:
#     print(f.read())

# #### modules
# import asgn_40 

# print(asgn_40.count_Char("this is a random sentence but it does have some 1234 also"))