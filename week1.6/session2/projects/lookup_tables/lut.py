# Week 1.6, Session 2: Look-up Tables

"""
Classes for look-up tables, used to change the brightness of an image.
"""


class LookupTable:
    """
    A look-up table that maps each pixel value (0-255) to a new value.
    """

    def __init__(self):
        """
        Creates an identity LUT, which leaves every pixel value unchanged.
        """
        self.table = list(range(256))

    def set(self, value, new_value):
        """
        Changes the LUT so that the given pixel value maps to new_value.
        """
        self.table[value] = new_value

    def display(self):
        """
        Prints the mapping performed by this LUT.
        """
        for value in range(256):
            print(f"{value} -> {self.table[value]}")

    def apply(self, image):
        """
        Returns a new Image with this LUT applied to the given image.
        """
        result = image.copy()
        self.apply_in_place(result)
        return result

    def apply_in_place(self, image):
        """
        Applies this LUT to the given image, changing the image directly.
        """
        for i in range(image.width * image.height):
            image[i] = self.table[image[i]]


class InverseLUT(LookupTable):
    """
    LUT that inverts the brightness, so white becomes black.
    """

    def __init__(self):
        super().__init__()
        for value in range(256):
            self.set(value, 255 - value)


class BrightnessLUT(LookupTable):
    """
    LUT that makes the image brighter by adding a fixed amount to each pixel.
    """

    def __init__(self, amount=40):
        super().__init__()
        for value in range(256):
            new_value = value + amount
            if new_value > 255:
                new_value = 255
            self.set(value, new_value)


class ContrastLUT(LookupTable):
    """
    LUT that increases contrast by stretching values away from the middle.
    """

    def __init__(self):
        super().__init__()
        for value in range(256):
            new_value = 128 + (value - 128) * 2
            if new_value < 0:
                new_value = 0
            if new_value > 255:
                new_value = 255
            self.set(value, new_value)
