# pick6.py
from random import randint


def pick6():
    """
    returns a list of 6 random numbers; from 1-99
    """
    # local_pick6_list = []
    # for num in range(6):
    #     num = random.randint(1, 99)
    #     local_pick6_list.append(num)
    # return local_pick6_list
    return [randint(1, 99) for n in range(6)]  # same as above


def num_matches(winning, ticket):
    """
    returns the amount of matching numbers at the same index in 2 different lists
    >>> num_matches([1,2,3,4,5], [1,3,3,5,5])
    3
    >>> num_matches([1,2,3,4,5], [5,4,3,2,1])
    1
    """
    counter = 0
    for num in range(len(ticket)):
        if winning[num] == ticket[num]:
            counter += 1

    return counter


balance = 0
winning_ticket = pick6()

for outcomes in range(100000):
    ticket = pick6()

    if num_matches(winning_ticket, ticket) == 1:
        balance += 2
    if num_matches(winning_ticket, ticket) == 2:
        balance += 5
    if num_matches(winning_ticket, ticket) == 3:
        balance += 98
    if num_matches(winning_ticket, ticket) == 4:
        balance += 49998
    if num_matches(winning_ticket, ticket) == 5:
        balance += 999998
    if num_matches(winning_ticket, ticket) == 6:
        balance += 24999998
    if num_matches(winning_ticket, ticket) == 0:
        balance += -2
print(f'The winning ticket is {winning_ticket}')


def place_value(number):
    return ("{:,}".format(number))


print(f'Your ending balance is ${place_value(balance)}')
