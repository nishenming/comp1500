# Week 1.6, Session 2: Look-up Tables demo

"""
Reads a PGM image, applies a look-up table to it, and writes the result
out to a new PGM file.

Usage: python lut_demo.py input.pgm output.pgm invert|brighten|contrast
"""

import sys

from image import Image
from lut import InverseLUT, BrightnessLUT, ContrastLUT


def main():
    if len(sys.argv) != 4:
        print("usage: python lut_demo.py input.pgm output.pgm invert|brighten|contrast")
        sys.exit(1)

    in_name = sys.argv[1]
    out_name = sys.argv[2]
    choice = sys.argv[3]

    if choice == "invert":
        lut = InverseLUT()
    elif choice == "brighten":
        lut = BrightnessLUT()
    elif choice == "contrast":
        lut = ContrastLUT()
    else:
        print(f"unknown LUT: {choice}")
        sys.exit(1)

    image = Image.read(in_name)
    result = lut.apply(image)
    result.write_pgm(out_name)

    print(f"read {in_name} ({image.width} x {image.height})")
    print(f"applied {choice} LUT")
    print(f"wrote {out_name}")


if __name__ == "__main__":
    main()
