
height = float(input("Input your height in Feet: "))
weight = float(input("Input your weight in Pounds: "))

print("Your body mass index is: ", (weight / (height * height), 2))


print("Input your height: ")
height_ft = int(input("Feet: "))
height_inch = int(input("Inches: "))
height_inch += height_ft * 12
height_cm = round(height_inch * 2.54, 1)

print("Your height is : %d cm." % height_cm)


print("Input your wweight: ")
weight_lbs = int(input("Pounds: "))
weight_kg = round(weight_lbs /2.2)

print("Your weight is :  kg." % height_kg)

height_cm = float(input("Input your height in Centermeters: "))
weight_kg = float(input("Input your weight in Kilograms: "))

print("Your body mass index is: ", (weight_kg / (height_cm * height_cm), 2))