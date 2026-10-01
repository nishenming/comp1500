# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}")
print(f"Modified String 1: {user_string.lower()}")# make all letters small
print(f"Modified String 2: {user_string.upper()}")# make all letters big
print(f"Modified String 3: {user_string.strip()}")# delete spaces at start and end
print(f"Modified String 4: {user_string.replace('a', '@')}")# chang"a" to "@"
print(f"Modified String 5: {user_string.capitalize()}")# only first letter big
print(f"Modified String 6: {user_string[::-1]}")# reverse the text
print(f"Modified String 7: {user_string.title()}")# each word first letter big 
print(f"Modified String 8: {len(user_string)}")# count how many characters
print(f"Modified String 9: {user_string.find('a')}")# find first place of "a"
print(f"Modified String 10: {user_string.count('a')}")# count how many "a"
print(f"Modified String 11: {user_string.startswith('Hello')}")# check if start with Hello 
print(f"Modified String 12: {user_string.endswith('!')}")# check if end with !
print(f"Modified String 13: {user_string.isalnum()}")# letters or number
print(f"Modified String 14: {user_string.isalpha()}")# only letters
print(f"Modified String 15: {user_string.isdigit()}")# only number



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!