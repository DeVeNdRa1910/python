import math

def calculate(r):
    area = math.pi * (r ** 2)
    circumference = 2 * math.pi * r
    return area, circumference

print(calculate(10))