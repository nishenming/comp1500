# Week 1.5, Session 2: Task 1

# Add type hints to the Point class

import math


class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x
        self.y = y

    def distance(self) -> float:
        """
        Returns distance of this Point from the origin.
        """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def distance_to(self, p: "Point") -> float:
        """
        Returns distance of this Point from the specified Point.
        """
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)


# Test program

p = Point("two", "one")
print(p.distance())
