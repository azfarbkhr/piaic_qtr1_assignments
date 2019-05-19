'''
REQUIREMENTS
6. Write a Python program to get the volume of a sphere, please take the radius as input from user. V=4 / 3 πr3
'''

# print requirements
print("Requirements: a Python program to get the volume of a sphere, please take the radius as input from user")
print()


# variables used
radius = 0
volumeOfSphere = 0


# input from user
while True:
    try:
        radius = int(input("Please enter radius of sphere (cm): "))
        if radius <= 0:
            raise ZeroDivisionError
        break
    except ValueError:
        print("Error 01: You have entered an invalid number.")
    except ZeroDivisionError:
        print("Error 02: You have entered a number less than or equal to zero.")


# calculating area
volumeOfSphere = round((4 / 3) * (22 / 7) * (radius ** 3), 2)


# printing result
print("the volume of this sphere is {x} centimeter cube".format(x = volumeOfSphere))