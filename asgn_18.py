'''
Requirements
18.	Write a Python program to calculate the hypotenuse of a right angled triangle. 
'''

# variables used
length = 21
breadth = 15
hypotenuse = 0


# logic 
def calcHypotenuse(l, b):
    return round(((l ** 2) + (b ** 2)) ** (1 / 2), 2)


# print output 
print (calcHypotenuse(length, breadth))