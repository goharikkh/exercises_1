import math
radius = float(input('Enter the Radius of a Cylinder '))
height = float(input('Enter the Height of a Cylinder '))

def cylinder_vol(r, h):
    return math.pi * r**2 * h

print(cylinder_vol(radius, height))