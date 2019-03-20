#gradinglab.py
user_grade = input("What did you get on Mrs. Armstrong's unit exam?\n >")
user_grade = int(user_grade)
ones_digit = user_grade % 10
if ones_digit <= 4:
    sign = '-'
if ones_digit == 5:
    sign = ' '
if ones_digit >= 6:
    sign = '+'
if user_grade <= 59 :
    print(f"An F!?")
if user_grade == 100:
    sign = ' '
if user_grade > 59 and user_grade < 70 :
    print(f"D{sign}? At least you didn't fail...")
if user_grade > 69 and user_grade < 80 :
    print(f"C{sign}...There's some room for improvement.")
if user_grade > 79 and user_grade < 90 :
    print(f"B{sign}, not too shabby.")
if user_grade > 89 and user_grade <= 100 :
    print(f"Way to go, an A{sign}!")
