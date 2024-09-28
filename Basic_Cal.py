calcmessage = input("Enter a math calculation: ")

parameters = calcmessage.split()
value1 = float(parameters[0])
operator = parameters[1]
value2 = float(parameters[2])

result = None

# Calculation If Else Statements
if operator == "+":
    result = value1 + value2
elif operator == "-":
    result = value1 - value2
elif operator == "*":
    result = value1 * value2
elif operator == "/":
    if value2 != 0:  #
        result = value1 / value2
    else:
        result = "Error: Division by zero"


print(f"The result of {value1} {operator} {value2} is: {result}")
