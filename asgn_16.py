'''
Requirement
16.	Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). https://en.wikipedia.org/wiki/Euclidean_distance
'''

# values used
point1 = (300, 300)
point2 = (200, 200)

# logic 
def Euclidean_distance(p, q):
    return round ((((q[0] - p[0]) ** 2) + ((q[1] - p[1]) ** 2)) ** (1 / 2), 2)


# print output
print(Euclidean_distance(point1, point2))