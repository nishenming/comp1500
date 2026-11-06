"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""

destination = input("Where are you going to? ")

distance_miles_input = input("How many miles will you travel? ")
time_hours_input = input("How many hours will the journey take? ")

distance_miles = float(distance_miles_input)
time_hours = float(time_hours_input)

if distance_miles <= 0 or time_hours <= 0:
    print("The miles and the hours must be more than 0")
else:
    average_speed = distance_miles / time_hours
    print(f"Trip to {destination}: average speed {average_speed:.2f} miles per hour")
