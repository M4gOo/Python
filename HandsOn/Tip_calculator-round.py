print("Welcome to the tip calculator")
total = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to slipt the bill? "))
tip_percentage = tip/100

pay = round((total + (total * tip_percentage)) / people,2)

print(f"Each person should pay: ${pay}")
