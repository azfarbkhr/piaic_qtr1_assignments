'''
Requirements
13.	Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
'''

# variables used
firstInteger = 2
secondInteger = 7

# logic to compare numbers
def specialCompare(x, y):
    if x == y:
        return (True, "the 2 integers are equal")
    elif x + y == 5:
        return (True, "the sum of 2 integers is equal to 5")
    elif x - y == 5 or y - x == 5:
        return (True, "the difference of 2 integers is equal to 5")
    else:
        return (False, "the two given integer values are not equal and nor their sum or difference is 5")


# print logic
print(specialCompare(firstInteger, secondInteger)[1])