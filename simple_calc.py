#simple_calc.py

#dictionary of operations (keys are symbols, values are functions)
# operations = {'+': +, '-': -,'*': *, '/': /} #experimental

# This function adds two numbers
def add(x, y):
   return x + y
# This function subtracts two numbers
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y

validation = True

while validation:
    user_op = input("What operation would you like to perform? ('+', '-', '*','/','quit'):")


    if user_op == 'quit':
        validation = False

    elif user_op == '+' or user_op == '-' or user_op == '/' or user_op == '*':
        try:
                num1 = int(input("Enter first number: "))

                num2 = int(input("Enter second number: "))
                if user_op == '+':
                    print(f'{num1}{user_op}{num2}={add(num1,num2)}')
                if user_op == '-':
                    print(f'{num1}{user_op}{num2}={subtract(num1,num2)}')
                if user_op == '*':
                    print(f'{num1}{user_op}{num2}={multiply(num1,num2)}')
                if user_op == '/':
                    print(f'{num1}{user_op}{num2}={divide(num1,num2)}')



        except ValueError:
            print('Please enter a number')




    else:
        print("Sorry. I didn't get that.")


#prints final operation
