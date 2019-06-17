'''
Requirements
25.	Write a Python program to calculate the sum of the digits in an integer
'''

# variables used
n = 0

# get user input
while True:
    try:
        n = int(input("Please enter an integer to sum its digits: "))
        break
    except:
        print("Error 1: You have entered an invalid integer, please try again.")


# logic to convert
def get_sum_of_digits(number):
    if number < 0:      # if a number in negative then convert to positive so that code not crash
        number = number * -1 

    temp = str(number)
    sumOfdigits = 0
    for i in temp:
        sumOfdigits = sumOfdigits + int(i)
    return sumOfdigits

# print output
print(get_sum_of_digits(n))
