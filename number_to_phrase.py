# number_to_phrase.py

ones_dict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
tens_dict = {
    1: 'Ten', 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
    6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
teens_dict = {
    1: 'Eleven', 2: 'Twelve', 3: 'Thirteen', 4: 'Fourteen', 5: 'Fifteen',
    6: 'Sixteen', 7: 'Seventeen', 8: 'Eighteen', 9: 'Nineteen'
}

validation = True

while validation:
    user_response = input('Would you like to nameify? y/n: \n')
    if user_response == 'y':
        user_num = input('What number would you like us to type out? :')
        if user_num.isdigit():
            tens_dig = int(user_num)//10
            ones_dig = int(user_num) % 10
            if ones_dig == 0:
                print(tens_dict[tens_dig])
            elif tens_dig >= 1:
                if tens_dig == 1:
                    print(teens_dict[ones_dig])
                elif tens_dig != 1:
                    if ones_dig == 0:
                        print(tens_dict[tens_dig])
                    print(f'{tens_dict[tens_dig]}-{ones_dict[ones_dig]}')

                else:
                    print('Something went wrong')
            else:
                print(ones_dict[ones_dig])
        else:

            print('Please enter a number from 0-99')

    elif user_response == 'n':
        print('Goodbye')
        validation = False
    else:
        print('Not a valid response')
