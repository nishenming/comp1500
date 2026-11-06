# A bad class implementation

# What does the runtime error mean?
# __init__ has no "self", so Python puts the new object in x_coordinate
# and 1.5 in y_coordinate, and then 2.0 is one too many.
# How do we fix the code?
# Add self and store the values as self.x and self.y.

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
