'''
REQUIREMENTS
1.	Write a Python program which accepts the radius of a circle from the user and compute the area
'''

while True:
    try:
        radius = int(input("Please enter radius of circle: "))
        break
    except:
        print("Error 01: You have entered an incorrect number.")
    