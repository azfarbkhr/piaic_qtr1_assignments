'''
Requirement
12.	Write a Python program that will accept the base and height of a triangle and compute the area (https://www.khanacademy.org/math/basic-geo/basic-geo-area-and-perimeter/area-triangle/a/area-of-triangle)
Area = 1/2 * b * h
'''

# variables used
breadth = 10
height = 12


# logics to find area of triangle
def triangleFindArea(h, b):
    areaTriangle = 1 / 2 * h * b
    return areaTriangle

# print output
print(triangleFindArea(height, breadth))
