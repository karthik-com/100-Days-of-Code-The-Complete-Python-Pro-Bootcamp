## Project - Tip Calculator

# Solution -

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# Calculating tip
tip_percentage = (tip / 100) + 1
# Calculating bill for each person
bill_to_pay = (bill / people) * tip_percentage
print(f"Each person should pay: ${round(bill_to_pay, 2)}")