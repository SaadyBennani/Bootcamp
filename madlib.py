# madlib.py
sport_list = input("Give me 3 sports (seperated by commas)>")
sports2_list = sport_list.split(", ")

verb_list = input ("Give me 2 verbs (seperated by commas)>")
verb2_list = verb_list.split(", ")

adjective_list = input ("Give me 3 adjectives (seperated by commas)>")
adjective2_list = adjective_list.split(", ")

import random
sport_name = random.choice(sports2_list)
sport_adjective = random.choice(adjective2_list)
sport_verb = random.choice(verb2_list)
print(f"Playing {sport_name} can be a lot of fun. It's a great work-out, and most people would describe it as {sport_adjective}. It also really makes you {sport_verb}.")
