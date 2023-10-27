#INTRO TO IT 2nd COURSE
from math import sqrt
def heron_triangle_area(a, b, c):
    s = (a + b + c) / 2
    return round(sqrt(s*(s-a)*(s-b)*(s-c)))