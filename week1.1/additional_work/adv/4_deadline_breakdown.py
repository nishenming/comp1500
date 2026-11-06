"""Advanced Task 4: Deadline Breakdown
- Ask how many minutes remain until an assignment deadline.
- Use integer division and modulo to convert this number into days, hours, and minutes.
- Present the result using a formatted string such as "2 days, 3 hours, 15 minutes remaining".
- Extension: handle negative input by printing a warning that the deadline has already passed.
"""

minutes_remaining = int(input("Minutes remaining until the deadline: "))

if minutes_remaining < 0:
    print("The deadline has already passed")
else:
    minutes_in_day = 60 * 24
    days = minutes_remaining // minutes_in_day
    hours = (minutes_remaining % minutes_in_day) // 60
    minutes = minutes_remaining % 60
    print(f"{days} days, {hours} hours, {minutes} minutes remaining")
