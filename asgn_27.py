'''
Requirements
27.	Write a program to convert binary number to Decimal number

Usage this value "1010" should convert to 10
''' 

# variabled used
binaryNum = 10010


# logic to convert
def binary_to_decimal (number):
    decimalNum = 0
    temp = str(number)      # store num as a string variable so that we can iterate over its each digit
    index = 0               # this is an index of the position at which we stand when iterating over our number
    for i in reversed(temp):
        decimalNum = decimalNum + (int(i) * (2 ** index))
        index += 1
    return decimalNum


# print output
print("the binary value of {x} is equal to {y} in decimal.".format(x = binaryNum, y = binary_to_decimal(binaryNum)))