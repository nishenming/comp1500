# Week 4, Session 2: Task 4

# Given an incomplete recursive function power to calculate x raised to
# the power of n, your task is to complete the function.


def power(x, n):
    if n == 0:
        return 1

    return x * power(x, n - 1)


print(power(2, 5))     # 32
print(power(3, 4))     # 81
print(power(10, 0))    # 1
