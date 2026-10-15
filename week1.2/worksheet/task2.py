# Worksheet 1.2: Task 2 Solution

import sys
from util import read_numbers
numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")
    min_value = min(numbers)
    max_value = max(numbers)
mean_value = sum(numbers) / len(numbers)
sorted_list = numbers.copy()
sorted_list.sort()
list_length = len(sorted_list)
if list_length% 2 == 1:
    median_value = sorted_list[list_length // 2]
else:
    left_mid = sorted_list[(list_length // 2) - 1]
    right_mid = sorted_list[list_length // 2]
    median_value = (left_mid + right_mid) / 2

print(f"Minimum = {min_value}")
print(f"Maximum = {max_value}")
print(f"Mean = {mean_value}")
print(f"Median = {median_value}")
 
