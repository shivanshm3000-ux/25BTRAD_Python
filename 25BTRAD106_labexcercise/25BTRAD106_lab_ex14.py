# Lab 14: Bank account system using OOP

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance      # private attribute (encapsulation)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be positive.")
        else:
            self.__balance += amount
            print("Deposited", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawn", amount)

    def check_balance(self):
        print("Balance of", self.name, ":", self.__balance)

# Simulation of routine transactions
acc = BankAccount("Shivansh", 1000)
acc.check_balance()
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()

# Testing invalid transactions
acc.deposit(-100)
acc.withdraw(5000)
acc.withdraw(0)
acc.check_balance()
