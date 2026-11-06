"""Advanced Task 5: Safe Divider
- Ask for a numerator and a denominator.
- Convert both inputs to integers and divide them to get a result.
- Use try/except to catch both non-numeric input and division by zero, giving useful messages for each case.
- Only print the final answer when the calculation succeeds.
"""

numerator_input = input("Enter the numerator: ")
denominator_input = input("Enter the denominator: ")

try:
    numerator = int(numerator_input)
    denominator = int(denominator_input)
    answer = numerator / denominator
    print(f"{numerator} / {denominator} = {answer:.2f}")
except ValueError:
    print("That is not a number")
except ZeroDivisionError:
    print("You cannot divide by zero")
