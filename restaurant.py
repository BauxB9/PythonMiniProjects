# Bou Haidara
# Python Course
# 5 September
# M02 Programming Assignment
# Restaurant


# Get meal cost
meal_cost = float(input("Enter meal cost: $"))

# Tax (6.75%) and tip
tax = meal_cost * 0.0675
tip = (meal_cost + tax) * 0.18
100
# Get tip from user
tip = float(input(f"Suggested tip: ${tip:.2f}. Enter tip amount: $"))

# Total bill
total = meal_cost + tax + tip

# Receipt
print(
    f"Your total Meal: ${meal_cost:.2f}, Tax: ${tax:.2f}, Tip: ${tip:.2f}, Total: ${total:.2f}")
