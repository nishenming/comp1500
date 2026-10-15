# Worksheet 1.2: Task 1 Solution
import sys
num = input("please enter an integer of distinction")
if num.isdecimal() == False:
    sys.exit("Error: Grade must be an integer between 0 and 100")

grade = int(num)

if grade >=00 and grade <=39:
    print(f"{grade}is a Fail")
elif grade >=40 and grade <=69:
    print(f"{grade}is a Pass")
elif grade >=70 and grade <= 100:
    print (f"{grade}is a Distinction")
else:
    sys.exit("Error: Grade must be an integer between 0and 100")
