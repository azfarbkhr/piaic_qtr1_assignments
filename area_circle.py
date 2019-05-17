'''
REQUIREMENTS
1.	Write a Python program which accepts the radius of a circle from the user and compute the area
'''

while True:
    try:
        radius = int(input("Please enter radius of circle: "))
        if radius <= 0:
            raise ZeroDivisionError
        break
    except ValueError:
        print("Error 01: You have entered an invalid number.")
    except ZeroDivisionError:
        print("Error 02: You have entered a number less than or equal to zero.")


cricleArea = int((22 / 7) * (radius ** 2))

print("The area of circle is {x}".format(x = cricleArea))