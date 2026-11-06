# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.

filename = input("Name of the PGM file (for example feep.pgm): ")
path = "../images/" + filename

try:
    with open(path, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("I cannot find that image")
else:
    # skip the empty lines and the comment lines, keep the rest
    info = []
    for line in lines:
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        info.append(line)

    width, height = info[1].split()
    max_gray = info[2]

    # print image dimension (i.e., Dimensions: width x height pixels)
    print(f"Dimensions: {width} x {height} pixels")

    # print max gray value (i.e., Max Gray Value: max_gray_value)
    print(f"Max Gray Value: {max_gray}")
