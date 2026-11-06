"""Advanced Task 2: Budget Breakdown
- Ask for three separate expense amounts (for example: travel, food, accommodation).
- Convert each input so you can add them together to get a total trip cost.
- Calculate the average spend per category and show each value with an f-string.
- Extension: format the totals so they always show two decimal places.
"""

travel_cost = float(input("Travel cost in pounds: "))
food_cost = float(input("Food cost in pounds: "))
accommodation_cost = float(input("Accommodation cost in pounds: "))

total_cost = travel_cost + food_cost + accommodation_cost
average_cost = total_cost / 3

print(f"Travel cost: {travel_cost:.2f}")
print(f"Food cost: {food_cost:.2f}")
print(f"Accommodation cost: {accommodation_cost:.2f}")
print(f"Total cost: {total_cost:.2f}")
print(f"Average cost: {average_cost:.2f}")
