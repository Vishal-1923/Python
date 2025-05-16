# bank_accounts.py -> this file will hold the classes for several diff types of bank accounts.
# chapter20_oop_project.py -> import everything from our bank account.

from bank_accounts import * #means all

# creating an instance or object of a bank account
Vishal = BankAccount(1000, "Vishzzz")
Vishal.get_balance()
Vishal.deposit(1100)
Vishal.withdraw(10000)
Kumar = BankAccount(2000, "Kumar")
Kumar.get_balance()
Kumar.deposit(100)
Kumar.withdraw(100)
Vishal.transfer(111111, Kumar)

# creating a new interest benefit account
Vk = InterestRewardsAcct(5000, "VK")
Vk.get_balance()
Vk.deposit(100)
Vk.transfer(1, Vishal)

# savings acc.
Ap = SavingsAccount(10000, "AP")
Ap.get_balance()
Ap.withdraw(10000)
