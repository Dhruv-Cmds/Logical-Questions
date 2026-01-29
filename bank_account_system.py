# Author: Dhruv

# Create class BankAccount:
# Attributes:
# name
# balance
# Methods:
# deposit(amount)
# withdraw(amount)
# show_balance()
# Rules:
# Cannot withdraw more than balance.

class BankAccount:

    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def wintdraw (self , withdraw_amount):
        if (withdraw_amount > self.balance):
             print("Entered amount is more than balance.")
        
        elif (withdraw_amount < self.balance):
            self.balance = self.balance - withdraw_amount
            print(f"Total Balance :{self.balance}")

        elif (withdraw_amount == self.balance):
            self.balance = 0
            print("Total Balance :" , self.balance)

b = BankAccount ("Dhruv" ,15000)

withdraw_amount = int(input("Enter an amount :"))  

b.wintdraw(withdraw_amount)
print(f"Name of Account Holder is {b.name}. Total Balance is {b.balance}. Amount dabit {withdraw_amount}.")