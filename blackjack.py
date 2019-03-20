# blackjack.py

deck_of_cards = {
    'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
}


def total_cards(first, second, third):
    """
    adds up the total value of three cards
    """
    cards_list = []
    cards_list.append(deck_of_cards[first])
    cards_list.append(deck_of_cards[second])
    cards_list.append(deck_of_cards[third])

    return sum(cards_list)


validation = True

while validation:
    user_response = input('Would you like some Blackjack advice? y/n: \n')

    if user_response == 'y':
        user_firstcard = input('What is your first card?: \n')
        user_secondcard = input('What is your second card?: \n')
        user_thirdcard = input('What is your third card?: \n')
        if total_cards(user_firstcard, user_secondcard, user_thirdcard) < 17:
            print(f'{total_cards(user_firstcard, user_secondcard, user_thirdcard)} Hit!')
        elif total_cards(user_firstcard, user_secondcard, user_thirdcard) >= 17 and total_cards(user_firstcard, user_secondcard, user_thirdcard) < 21:
            print(f'{total_cards(user_firstcard, user_secondcard, user_thirdcard)} Stay!')
        elif total_cards(user_firstcard, user_secondcard, user_thirdcard) == 21:
            print(f'{total_cards(user_firstcard, user_secondcard, user_thirdcard)} Blackjack!')
        else:
            print(f'{total_cards(user_firstcard, user_secondcard, user_thirdcard)} Already Busted!')

    elif user_response == 'n':
        print('Goodbye')
        validation = False
    else:
        print('Not a valid response')
