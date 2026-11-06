# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

try:
    with open("student_data.csv", "r") as file:
        data = file.readlines()
except FileNotFoundError:
    print("I cannot find student_data.csv")
else:
    # Open a file called 'report.txt'
    with open("report.txt", "w") as report:
        # Read each student's grades and calculate their average grade
        for line in data[1:]:
            parts = line.strip().split(",")

            student_id = parts[0]
            name = parts[1]
            maths = int(parts[2])
            science = int(parts[3])
            history = int(parts[4])

            average = (maths + science + history) / 3

            # Write each student's name and their average grade to the report
            report.write(f"{name}: {average:.2f}\n")

    print("The report is saved in report.txt")
