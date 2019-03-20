#guess_the_number.py
import random
computer_choice = random.randint(1,10)
counter = 0


while True:
    try:
        user_choice = int(input("Guess a number between 1 and 10 \n>"))
        counter = counter + 1
        if user_choice == computer_choice:

            print(f"Yes, that was it! It only took you {counter} tries." )
            break
        elif user_choice != computer_choice:
            if user_choice > computer_choice:
                print("That wasn't it, try a lower number!")
            if user_choice < computer_choice:
                print("That wasn't it, try a higher number!")
            if user_choice == computer_choice:
                print("Yes, that was it! It only took you {counter} tries.")
    except ValueError:
        print('Please enter a number')
