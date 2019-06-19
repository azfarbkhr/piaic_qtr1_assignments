'''
Requirement
32.	Write a Python program to get the least common multiple (LCM) of two positive integers (https://en.wikipedia.org/wiki/Least_common_multiple)
'''

# variables used 
a = 336
b = 360

# logic used
def find_lcm(a, b):
    if a > b:
        lcm = a
    else:
        lcm = b

    while True:
        if (lcm % a == 0) and (lcm % b == 0):
            return lcm
        lcm += 1


# print output
print(find_lcm(a, b))
        