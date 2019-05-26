length = 4



# logic for following triangle
#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************

# for i in range(length):
#     for j in range(length - 1, i, -1):
#         print(" ", end = "")
#     for k in range((2 * i) + 1):
#         print("*", end = "")
#     for j in range(length - 1, i, -1):
#         print(" ", end = "")
#     print("")

# _____________________________________________________________________________________________________________________

# logic for following triangle
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

# for i in range(length):
#     for j in range(i + 1):
#         print("*", end = " ")
#     print("")
# for i in range(length - 1):
#     for j in range(length - i -1):
#         print("*", end = " ")
#     print("")


# ________________________________________________________________________________________________________
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

for i in range(5):
    for j in range(5-i-1):
        print(" ", end = " ")
    for k in range(i + 1):
        print("*", end = " ")
    print("")