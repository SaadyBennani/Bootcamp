# atm.py


class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        """
        returns the account balance
        """
        print(f'your account balance is ${self.balance}')

    def deposit(self, amount):
        """
        deposits the given amount into the account
        """
        self.balance += amount
        self.transactions.append(f'user deposited ${amount}')
        print(f'you have deposited ${amount} into your account; your new balance is ${self.balance}')

    def check_withdrawal(self, amount):
        """
        returns true if the withdrawn amount won't put the account in the negative
        """

        return amount <= self.balance

    def withdrawal(self, amount):
        """
        withdraws the amount from the account and returns it
        """
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.transactions.append(f'user withdrew ${amount}')
            print(f'you have withdrawn ${amount} from your account; your new balance is ${self.balance}')
        else:
            print('Insufficient funds')

    def print_transactions(self):
        """
        prints a log of user deposits and withdrawals
        """
        for transaction in self.transactions:
            print(transaction)


my_account = ATM()

loop = True

valid_inputs = [
        'c', 'check',
        'd', 'deposit',
        'w', 'withdrawal',
        'r', 'recent',
        'x', 'exit', 'quit',
        'h', 'help']

commands = """
    Commands:
    (c)heck balance
    (d)eposit
    (w)ithdrawl
    (r)ecent transactions
    e(x)it
    """

print('*************** ATM ***************')


while loop:
    print(commands)
    user_cmd = input('Please select a command\n>')

    if user_cmd in ['c', 'check']:
        my_account.check_balance()

    elif user_cmd in ['d', 'deposit']:
        dep_amount = int(input('How much would you like to deposit? \n>$'))
        my_account.deposit(dep_amount)

    elif user_cmd in ['w', 'withdrawal']:
        with_amount = int(input('How much would you like to withdraw? \n>$'))
        my_account.withdrawal(with_amount)

    elif user_cmd in ['r', 'recent']:
        my_account.print_transactions()

    elif user_cmd in ['x', 'exit', 'quit']:
        print('Goodbye')
        loop = False
    else:
        print('Not a valid response')
        print(commands)
