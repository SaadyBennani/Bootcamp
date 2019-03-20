# passwordgen.py
import random
import string

uppercase_list = string.ascii_uppercase
lowercase_list = string.ascii_lowercase
numbers_list = string.digits
symbols_list = ['!', '@', '#', '$', '%', '^', '&', '*']
password_length = int(input("How many characters would you like your password to be \n>"))
amount_upper = int(input("How many uppercase letters must it contain \n>"))
amount_lower = int(input("How many lowercase letters must it contain \n>"))
amount_symbols = int(input("How many symbols must it contain \n>"))
amount_digits = int(input("How many numbers must it contain \n"))

out_upper = ''
out_lower = ''
out_symbol = ''
out_digit = ''
out_string = ''

# password components

for num in range(0, amount_upper):
    out_upper += random.choice(uppercase_list)
    print(out_upper)

for num in range(0, amount_lower):
    out_lower += random.choice(lowercase_list)
    print(out_lower)
for num in range(0, amount_symbols):
    out_symbol += random.choice(symbols_list)
    print(out_symbol)

for num in range(0, amount_digits):
    out_digit += random.choice(numbers_list)
    print(out_digit)

# brings the password components together

for num in range(0, 1):
    out_string += out_upper + out_lower + out_symbol + out_digit

l = list(out_string)
random.shuffle(l)
password = ''.join(l)


# ensures password meets length requirement
if len(password) < password_length:
    password += random.choice(l)

# final password
print(("Your password is: \n ") + (password))
