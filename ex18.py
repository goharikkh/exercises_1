import math
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

s1 = float(input('Enter the s1: '))
s2 = float(input('Enter the s2: '))
s3 = float(input('Enter the s3: '))
print(triangle_area(s1, s2, s3))
