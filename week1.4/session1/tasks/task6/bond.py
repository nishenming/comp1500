# Week 4, Session 1: 

# You are given an incomplete function isBond with a docstring. Your task
# is to complete the function based on the details in the docstring.


def isBond(intList):
    """
    This function accepts a list of integers and returns True if the
    sequence 0, 0, 7 appears in the list, in that order. Return False
    otherwise. The numbers do not need to be consecutive, but must appear
    in the specified order.
    """

    found = 0
    for number in intList:
        if found == 0 and number == 0:
            found = 1
        elif found == 1 and number == 0:
            found = 2
        elif found == 2 and number == 7:
            found = 3

    return found == 3

# Check if the following lines of code produce the correct output
print(isBond([1, 2, 4, 0, 0, 7, 5]))   # True
print(isBond([1, 0, 2, 4, 0, 5, 7]))   # True
print(isBond([1, 7, 2, 0, 4, 5, 0]))   # False
