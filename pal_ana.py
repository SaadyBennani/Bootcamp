# pal_ana.py


validation = True

while validation:
    user_response = input('Would you like to check for (a)nagram, (p)alindrome, or (q)uit?: \n')

    if user_response == 'a':
        first_word = input("What is your first word? >")
        second_word = input("What is your second word? >")
        first_word = first_word.replace(" ", "")
        first_word = first_word.lower()
        second_word = second_word.replace(" ", "")
        second_word = second_word.lower()

        first_list = list(first_word)
        second_list = list(second_word)

        first_list.sort()
        second_list.sort()

        if first_list == second_list:
            print(f"{first_word} is an anagram of {second_word} !")

        else:
            print(f"{first_word} is not an anagram of {second_word} !")

    elif user_response == 'p':

        word = input("What is your word?")
        word = word.replace(" ", "")
        word = word.lower()
        word_list = list(word)
        word_reversed = word_list[::-1]

        if word_list == word_reversed:
            print(f'{word} is a palindrome!')
        else:
            print(f'{word} is not a palindrome')

    elif user_response == 'q':
        print('Goodbye')
        validation = False

    else:
        print('Not a valid response')
