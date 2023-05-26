#Input Validation

#netincome = int(input("\tTotal earings: "))
investments = float(input("\n\tInvestments: "))
nonTaxable = float(input("\n\tNon Taxable Income: "))
salary = float(input("\n\tAre salaried (if not put a zero here): "))
rate = float(input("\n\tAre you hourly (place rate here, if not put a zero here): "))
hours = float(input("\n\tHow many hours do you work a week: "))
weeks = int(input("\n\tHow many weeks have you worked this month: "))
hourlyTotal = (hours*weeks*rate)

rent = float(input("\n\tRent: "))
car = float(input("\n\tCar Payment/Insurence: "))
utilities = float(input("\n\tUtilities: "))
cell = float(input("\n\tCell phone bill: "))
food = float(input("\n\tFood:  "))

print("\n\tTotal income:",investments+nonTaxable+salary+hourlyTotal)

print("\n\tTotal expenses:",rent+car+utilities+cell+food)

print("\n\tTake home:",(investments+nonTaxable+salary+hourlyTotal)-(rent+car+utilities+food+cell))
	