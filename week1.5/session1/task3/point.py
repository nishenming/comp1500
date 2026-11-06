# Week 1.5, Session 1: Task 3

import math

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self):
        """
        Returns the distance of this Point from the origin.
        """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def distance_to(self, p):
        """
        Returns the distance of this Point from another Point.
        """
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)


p1 = Point(3.0, 4.0)
print(f"x = {p1.x}, y = {p1.y}")
print(f"distance from the origin = {p1.distance()}")

p2 = Point(0.0, 0.0)
print(f"distance from p1 to p2 = {p1.distance_to(p2)}")
