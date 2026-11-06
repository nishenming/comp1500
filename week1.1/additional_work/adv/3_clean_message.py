"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = input("Type a message to tidy: ")

cleaned_message = raw_message.strip()
cleaned_message = cleaned_message.replace("  ", " ")
cleaned_message = cleaned_message.title()

print(f"Original: {raw_message}")
print(f"Cleaned: {cleaned_message}")
print(f"Characters before: {len(raw_message)}")
print(f"Characters after: {len(cleaned_message)}")
