# rot_cipher.py
import string
english = list(string.ascii_lowercase)


# my approach
# def shift(l, n):
#     return l[n:]+l[:n]
#
# rot_13 = shift(english,13)
#
# translate = dict(zip(english, rot_13))
#
#
# def encode(string):
#     encoded = ''
#     for char in string:
#         encoded+= translate[char]
#     return encoded


# in class ex
def cypher(message, n, decode=False):
    n %= 26  # wrap around 26
    translate = english[n:] + english[:n]

    if decode:
        translate = dict(zip(translate, english))

    else:
        # encode logic
        translate = dict(zip(english, translate))

    coded = ''
    for char in message:
        coded += translate.get(char, char)
    return coded


def main():
    replay = True
    print('~'*70)
    print('Cypher-Matic 3000')
    print('~'*70)
    while replay:  # loop game

        while True:  # input validation
            operation = input('Would you like to (e)ncode or (d)ecode: ').strip().lower()
            if operation in ['encode', 'e', 'decode', 'd']:
                break

        while True:  # input validation
            try:
                n = int(input('How much do you want to rotate by: '))
                break
            except ValueError:
                print('Error: enter a number.')

        message = input('Enter message to cypher: ')

        if operation.startswith('e'):
            operation = 'encoded'
            decode = False
        else:
            operation = 'decoded'
            decode = True

        print('~'*70)
        print(f'Here is your {operation} message: ')
        print(cypher(message, n, decode))
        print('~'*70)

        while True:  # input validation
            play_again = input('Do you want to play again: ').strip().lower()
            if play_again in ['yes', 'y', 'no', 'n']:
                break

        if play_again.startswith('n'):
            replay = False
            print('~'*70)
            print('Goodbye!')
            print('~'*70)


if __name__ == '__main__':
    main()
