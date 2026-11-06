# Week 1.3, Session 2: Log Data Filtering

# We want to find all failed login attempts based on Request and Status code 
# (i.e., POST /login with the response 401) in a log file and print these out in a
# human-readable format.

# open and read the file

try:
    with open("site.log", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("I cannot find site.log")
else:
    # find all failed login attempts (POST /login with the response 401)
    for line in lines[1:]:
        parts = line.strip().split(",")

        date = parts[0]
        time = parts[1]
        ip_address = parts[2]
        request = parts[4]
        status_code = parts[5]

        if request == "POST /login" and status_code == "401":
            # print these out in a human-readable format
            print(f"IP address {ip_address} failed to login at {time} on {date}")

# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
