# Week 1.3, Session 2: Invert PGM image

# Open a pgm image file to read
# You can use the relative path ../images/filename
# You could handle file errors with try/except

filename = input("Name of the PGM file (for example feep.pgm): ")
path = "../images/" + filename

try:
    with open(path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("I cannot find that image")
else:
    data = []
    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        data.append(line)

    width, height = data[1].split()
    width = int(width)
    height = int(height)
    max_gray = int(data[2])

    pixels = []
    for line in data[3:]:
        row = []
        for value in line.split():
            row.append(int(value))
        pixels.append(row)

    # Create inverted image
    # the formula: invert_pixel_value = max_gray - original_pixel_value
    inverted = []
    for row in pixels:
        new_row = []
        for value in row:
            new_row.append(max_gray - value)
        inverted.append(new_row)

    # write the inverted pgm image to a new file
    new_filename = "inverted_" + filename

    with open(new_filename, "w") as out:
        out.write("P2\n")
        out.write(str(width) + " " + str(height) + "\n")
        out.write(str(max_gray) + "\n")

        for row in inverted:
            line = " ".join(str(value) for value in row)
            out.write(line + "\n")

    print(f"The inverted image is saved in {new_filename}")
