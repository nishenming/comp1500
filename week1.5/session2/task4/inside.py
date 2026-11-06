# Week 1.5, Session 2: Task 4

from geometry import Point, Circle

circle = Circle(5.0, Point(0.0, 0.0))

print(f"circle: {circle}")

p1 = Point(1.0, 2.0)
p2 = Point(6.0, 0.0)

print(f"{p1} in circle: {p1 in circle}")
print(f"{p2} in circle: {p2 in circle}")
