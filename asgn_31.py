'''
Requirements
31.	Write a Python program to compute the greatest common divisor (GCD) of two positive integers. (https://en.wikipedia.org/wiki/Euclidean_algorithm)
'''

# variables used
a = 150
b = 200

# logic 
def find_gcd (a, b):
    gcd = 0
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    
    return gcd


# print output
print("the greatest common divisor for variables {x} and {y} is {z}.".format(
    x = a,
    y = b,
    z = find_gcd(a, b)
))