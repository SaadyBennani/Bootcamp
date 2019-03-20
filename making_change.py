# lab9_making_change.py

while True: #input validation

    total_pennies = input("How much money do you have? \n>").strip().strip('$')

    try:
        total_pennies = round(float(total_pennies) * 100)
        if total_pennies <0:
            raise ValueError
        break
    except ValueError:
        print('Please enter a non-negative dollar amount')

total_quarters = total_pennies // 25
total_pennies %= 25
total_dimes = total_pennies // 10
total_pennies %= 10
total_nickles = total_pennies // 5
total_pennies %= 5

print(f"You have {int(total_quarters)} quarters, {int(total_dimes)} dimes, {int(total_nickles)} nickles, and {int(total_pennies)} pennies")
