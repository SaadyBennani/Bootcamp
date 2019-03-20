#rps.py

import random
def calc_winner(comp_choice, user_choice):
    defeats = {
        'rock':'scissors', 'paper':'rock', 'scissors':'paper'
        }

    if comp_choice == user_choice:
        return 'Tie'
    elif defeats[comp_choice] == user_choice:
        return 'Computer Wins'
    else:
        return 'User Wins'

rps = ['rock', 'paper', 'scissors']
while True:
    user_choice = input('Rock, Paper, or Scissors?').strip().lower()
    if user_choice not in rps:
        print("Please choose Rock, Paper, or Scissors")
        continue
    else:
        break

computer_choice = random.choice(rps)
print(computer_choice)

print(calc_winner(computer_choice, user_choice))
