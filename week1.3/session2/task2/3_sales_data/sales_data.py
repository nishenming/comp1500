# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data

try:
    with open("sales.csv", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("I cannot find sales.csv")
else:
    biggest_sale = 0
    biggest_day = ""
    total_sales = 0
    number_of_rows = 0
    widget_units = {}

    for line in lines[1:]:
        parts = line.strip().split(",")
        date = parts[0]
        product = parts[1]
        sale_amount = int(parts[2])
        units_sold = int(parts[3])

        total_sales = total_sales + sale_amount
        number_of_rows = number_of_rows + 1

        # find the largest sale day (highest sale amount)
        if sale_amount > biggest_sale:
            biggest_sale = sale_amount
            biggest_day = date

        # count the units sold for each widget
        if product in widget_units:
            widget_units[product] = widget_units[product] + units_sold
        else:
            widget_units[product] = units_sold

    # average sale amount
    average_sale = total_sales / number_of_rows

    # the widget which has been sold the most
    best_widget = ""
    best_units = 0
    for product in widget_units:
        if widget_units[product] > best_units:
            best_units = widget_units[product]
            best_widget = product

    print(f"Largest sale day: {biggest_day} with {biggest_sale}")
    print(f"Average sale amount: {average_sale:.2f}")
    print(f"Most sold widget: {best_widget}")

# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget
