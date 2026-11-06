# Another bad class implementation

# What does the runtime error mean?
# The values go into local variables x and y, not into the object,
# so the object has no attribute x.
# How do we fix the code?
# Store them as self.x and self.y.

class Point:
    """
    A point in 2D space.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate


p = Point(1.5, 2.0)
print(p.x)
print(p.y)
