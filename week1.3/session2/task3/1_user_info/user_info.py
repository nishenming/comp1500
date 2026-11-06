# Week 1.3, Session 2: Write User Information to a File

# Prompt the user for their name, age, and favorite colour.

name = input("What is your name? ")
age = input("How old are you? ")
colour = input("What is your favourite colour? ")

# Open a file called 'user_info.txt' for writing

# Write each piece of information to the file, each on a new line.

with open("user_info.txt", "w") as file:
    file.write(name + "\n")
    file.write(age + "\n")
    file.write(colour + "\n")

print("Your information is saved in user_info.txt")

# Hints:
# - Remember to add \n for new lines when writing to files


# Optional: extend this by using a loop to allow multiple people to enter their info in a row
# If you want multiple people to add info without overwriting, consider append mode 'a'
