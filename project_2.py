print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
bill_tip = tip / 100 * bill + bill
people_split = int(input("How many people to split the bill?"))
each_people = round((bill_tip / people_split), 2)
print(f"Each person should pay: ${each_people}")