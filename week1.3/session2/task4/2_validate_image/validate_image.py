# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

filename = input("Name of the PGM file (for example gradient.pgm): ")
path = "../images/" + filename

try:
    with open(path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("I cannot find that image")
else:
    # Read the file content
    data = []
    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        data.append(line)

    # Store the width, the height, and the maximum gray value
    width, height = data[1].split()
    width = int(width)
    height = int(height)
    max_gray = int(data[2])

    # the pixel values start after P2, the width/height and the max gray value
    pixels = []
    for line in data[3:]:
        row = []
        for value in line.split():
            row.append(int(value))
        pixels.append(row)

    # Check if the widths and heights are the same as specified
    if len(pixels) != height:
        print("Invalid height")
    else:
        wrong_width = False
        for row in pixels:
            if len(row) != width:
                wrong_width = True

        if wrong_width:
            print("Invalid width")
        else:
            # For each pixel, check if the pixel value is between 0 and the max gray value
            wrong_pixel = False
            for row in pixels:
                for value in row:
                    if value < 0 or value > max_gray:
                        wrong_pixel = True

            if wrong_pixel:
                print("Invalid pixel values")
            else:
                print("Valid image")
