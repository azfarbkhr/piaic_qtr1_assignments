'''
Requirement
19.	Write a Python program to convert the distance (in feet) to inches, yards, and miles. 1 feet = 12 inches, 3 feet = 1 yard, 5280 feet = 1 mile
'''

# variables used
ftDistance = 0 
inDistance = 0
ydDistance = 0
mlDistance = 0

while True:
    try:
        ftDistance = int(input("Please enter a number in feet to convert: "))
        if ftDistance < 0:
            raise ValueError
        break
    except:
        print("Error 01: You have entered an invalid input. only non-negative integers allowed")



# logic to convert
# feet to inches
def ft_to_in(ft):
    return round(ft * 12, 2)

# feet to yards
def ft_to_yd(ft):
    return round( ft / 3 , 2)

# feet to miles
def ft_to_ml(ft):
    return round( ft / 5280 , 4)


# print output
print("feet to inch: " + str(ft_to_in(ftDistance)))
print("feet to yard: " + str(ft_to_yd(ftDistance)))
print("feet to ml: " + str(ft_to_ml(ftDistance)))
