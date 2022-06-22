import math
r = input('Enter the radius of the circle ')


def circle_area(x):
    return math.pi * (x ** 2)


def sphere_volume(y):
    return 4.0 / 3.0 * (math.pi * (y ** 3))


print("area = ", circle_area(float(r)))
print("volume = ", sphere_volume(float(r)))
