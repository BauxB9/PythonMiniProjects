# Bou Haidara
# Python Course
# 5 September
# M02 Programming Assignment
# Planet Weight

# planets_weight.py

# Planetary gravity multiples
planets = {
    "Sun": 27.01, "Mercury": 0.38, "Venus": 0.91, "Earth": 1,
    "Moon": 0.166, "Mars": 0.38, "Jupiter": 2.34,
    "Saturn": 1.06, "Uranus": 0.92, "Neptune": 1.19, "Pluto": 0.06
}

# Get user name and weight
name = input("Enter your name: ")
weight = float(input("Enter your weight on Earth: "))

# Greet user and display weights on planets
print(f"\n{name}, your weight on other celestial bodies:")
for planet, gravity in planets.items():
    print(f"{planet}: {weight * gravity:.2f} lbs")
