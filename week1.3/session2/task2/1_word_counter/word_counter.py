# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

filename = input("Which file do you want to count? ")

try:
    with open(filename, "r") as file:
        text = file.read()
except FileNotFoundError:
    print("I cannot find that file")
else:
    # calculate the number of words
    words = text.split()

    # display the wordcount
    print(f"There are {len(words)} words in {filename}")

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210
