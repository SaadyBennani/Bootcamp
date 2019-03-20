# magic8.py
import random

iteration = True

while iteration:
    question = input("Hi, I'm here to help answer your questions. Feel free to ask me one\n>")
    response_list = ["Yes", "I don't think so.", "Only time will tell", "ABSOLUTELY NOT", "If you want it so"]
    if question == 'done':
        iteration = False
    else:
        print(random.choice(response_list))
