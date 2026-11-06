# To test that you can successfully download a file and upload it to gradescope

#Ask a user to enter two numbers (one per input)

try:
        number1 = int(input("enter first number: "))
        number2 = int(input("enter second number: "))
        answer = number1 * number2
        print(answer)
except ValueError:
        print("That is not a number")
