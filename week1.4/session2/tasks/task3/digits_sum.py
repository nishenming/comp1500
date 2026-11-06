# Week 4, Session 2: Task 4

# Given incomplete recursive function digits_sum with a docstring,
# your task is to complete the function based on the description


def digits_sum(number):
    """
    This recursive function calculates the sum of digits of a given positive
    integer. For example, sum of digits for 987 = 9 + 8 + 7 = 24.
    For simplisity, ignore the case when number is not an integer or
    not a positive integer.

    Args:
        number (int): The input is a positive integer.

    Returns:
        int: The sum of the digits of the input integer.
    """
    if number < 10:
        return number

    return number % 10 + digits_sum(number // 10)


def digits_sum_loop(number):
    total = 0
    while number > 0:
        total = total + number % 10
        number = number // 10
    return total


print(digits_sum(987))  # Output: 24
print(digits_sum(12345))  # Output: 15
print(digits_sum_loop(987))
print(digits_sum_loop(12345))
