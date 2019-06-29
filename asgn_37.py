'''
Requirement
37.	Write a Python program to reverse the digits of a given number and add it to the original, If the sum is not a palindrome repeat this procedure
'''

# variables used
digits = '1473'


# logic used
def is_palindrome (number):
    reversed_number = int(str(number)[::-1])
    sum_num = int(number) + reversed_number

    if sum_num == int(str(sum_num)[::-1]):
        return sum_num
    else:
        return is_palindrome (sum_num)


print(is_palindrome(digits))