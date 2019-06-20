'''
Requirement
39.	Write a Python program to create the multiplication table (from 1 to 10) of a number
'''

# variables used
number = 1201


# print output
for i in range(1, 11):
    print("{i} x {n} = {z}".format(i = i, n = number, z = i * number))
