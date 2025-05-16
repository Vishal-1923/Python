class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, acc_name):
        self.balance = initial_amount
        self.name = acc_name
        print(f"\n{self.name}'s account created.\nBalance = ${self.balance:.2f}")
    
    def get_balance(self):
        print(f"\n{self.name} has {self.balance:.2f} amount left.")
    
    def deposit(self, amount):
        self.balance += amount
        # print(f"\nDeposit complete. \n{self.name} has now {self.balance:.2f} amount left.")
        # we'll do something better
        print("\nDeposit complete.")
        self.get_balance()
    
    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account {self.name} only has {self.balance:.2f} amount.")
    
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except BalanceException as err:
            print(f"\nWithdraw interrupted: {err}.")

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. :)')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete...\n\n**********")
        except BalanceException as err:
            print(f"\nTransfer interrupted. X{err}")

class InterestRewardsAcct(BankAccount): #inheritance
    def deposit(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("\nDeposit completed.")
        self.get_balance()

class SavingsAccount(InterestRewardsAcct):
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee = 5
    # basically, whenever someone withdraws money additional 5% fee will be there.
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdrawl Complete...")
            self.get_balance()
        except BalanceException as err:
            print(f'Withdrawn interrupted: {err}')

