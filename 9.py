import math 

def vol_sphere(radius: int):
    return((4/3) * math.pi * pow(radius, 3))

print(vol_sphere(int(input())))
