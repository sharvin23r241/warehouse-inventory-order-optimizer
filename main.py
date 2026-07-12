import csv

print("=================================")
print(" Warehouse Order Optimizer ")
print("=================================\n")

warehouse = {}

# Read products from CSV
with open("products.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        warehouse[row["Item"].lower()] = row

# Ask the user for items
user_input = input("Enter items (comma separated): ")

items = user_input.lower().split(",")

print("\nItems Found:\n")
total_distance = 0
previous_x = 0
previous_y = 0

for item in items:
    item = item.strip()

    if item in warehouse:
        print(f"{warehouse[item]['Item']} -> Shelf {warehouse[item]['Shelf']} ({warehouse[item]['X']},{warehouse[item]['Y']})")
        current_x = int(warehouse[item]["X"])
        current_y = int(warehouse[item]["Y"])

        distance = abs(current_x - previous_x) + abs(current_y - previous_y)

        total_distance += distance

        previous_x = current_x
        previous_y = current_y
    else:
        print(f"{item} not found in warehouse.")

print("\n------------------------")
print(f"Total Distance : {total_distance} units")

estimated_time = total_distance * 2

print(f"Estimated Walking Time : {estimated_time} seconds")