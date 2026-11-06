# Week 4, Session 2: Task 2

# We can specify a 2d coordinate point with a tuple p=(x,y)
# Complete two functions to compute the mid-point and distance between 2 points.

import math

def midpoint(p1,p2):
    mid_x = (p1[0] + p2[0]) / 2
    mid_y = (p1[1] + p2[1]) / 2
    mid_point = (mid_x, mid_y)
    return mid_point

def length(p1,p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    distance = math.sqrt(dx * dx + dy * dy)
    return distance
    

m = midpoint( (0,0), (4,3) )    # mid = (2.0, 1.5)
d = length( (0,0), (4,3) )    # dist=5.0

print(f"Distance {d} Midpoint {m}")
