# Week 1.5, Session 1: Task 4

from geometry import Point, Circle

x_input = input("x coordinate of the centre: ")
y_input = input("y coordinate of the centre: ")
radius_input = input("radius of the circle: ")

centre = Point(float(x_input), float(y_input))
circle = Circle(float(radius_input), centre)

area = circle.area()
perimeter = circle.perimeter()

print(f"Area: {area:.4f}")
print(f"Perimeter: {perimeter:.4f}")
