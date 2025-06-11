import random

class BankAccounts:
    accounts = 0  # Class variable to keep track of total number of accounts
    all_accounts = {}  # Class dictionary to store all accounts for easy access

    def __init__(self, name, balance):
        """
        Initializes a new bank account if the initial balance meets the minimum requirement.
        """
        if balance >= 1000:
            self.name = name
            self.balance = balance
            # Generate a random 10-digit account number as a string
            self.account_number = str(random.randint(10**9, 10**10 - 1))
            BankAccounts.counter()  # Increment the accounts counter
            # Store this account instance in the class dictionary
            BankAccounts.all_accounts[self.account_number] = self
            # Create a transaction history with the opening entry
            self.history = [f"Account opened with Rs.{balance}"]
        else:
            raise ValueError("Minimum Balance to open an account is Rs 1000/-")

    @classmethod
    def counter(cls):
        """
        Increments the total number of bank accounts.
        """
        cls.accounts += 1

    def showTotal(self):
        """
        Displays the total number of accounts.
        """
        print(f"Total number of accounts are: {self.accounts}\n")
    
    @staticmethod
    def greet():
        """
        Prints a greeting message for new account holders.
        """
        print("Greetings! Thank you for opening an account with us!\n")

    def showData(self):
        """
        Displays the account holder's name, account number, and current balance.
        """
        print(f"The name of the account holder is {self.name}, the account number is {self.account_number} and the current balance is Rs {self.balance}/-\n")

    def deposit(self, amount):
        """
        Deposits the specified amount into the account and updates the history.
        """
        self.balance += amount
        print(f"Deposited Rs.{amount}, New Current Balance = {self.balance}\n")
        self.history.append(f"Deposited Rs{amount}")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds exist and updates the history.
        """
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn Rs.{amount}, New Current Balance = {self.balance}\n")
            self.history.append(f"Withdrawn Rs{amount}")
        else:
            print("Error In Withdrawing, Given amount exceeds available amount :(\n")

    def showHistory(self):
        """
        Prints the transaction history for the account.
        """
        print(f"Transaction history for account {self.account_number}:")
        for entry in self.history:
            print(entry)
        print()

    def acc_summary(self):
        """
        Displays the current balance and recent transactions.
        """
        print(f"Current Balance is: {self.balance}\n")
        print("Your recent transactions are as follows:\n")
        for entry in self.history:
            print(entry)
        print()

    @classmethod
    def deleteAcc(cls, acc_number):
        """
        Deletes an account by account number if it exists.
        """
        if acc_number in cls.all_accounts:
            del cls.all_accounts[acc_number]
            cls.accounts -= 1
            print("Account Deleted Successfully\n")
        else:
            print("Account Not Found, Please Ensure that the account number is correct.\n")

# ----- Usage demonstration -----
# Use all functions at least once

# Greet new customers
BankAccounts.greet()

# Create three accounts
acc1 = BankAccounts("Chirag", 15000)
acc2 = BankAccounts("Juhi", 25000)
acc3 = BankAccounts("Jai", 15000)

# Show total accounts
acc1.showTotal()

# Display account data for each account
acc1.showData()
acc2.showData()
acc3.showData()

# Deposit and withdraw operations
acc1.withdraw(1200)
acc1.deposit(800)
acc2.withdraw(1200)
acc2.deposit(800)
acc3.withdraw(1200)
acc3.deposit(800)

# Show transaction history for each
acc1.showHistory()
acc2.showHistory()
acc3.showHistory()

# Show account summary for each
acc1.acc_summary()
acc2.acc_summary()
acc3.acc_summary()

# Delete an account and show total again
BankAccounts.deleteAcc(acc2.account_number)
acc1.showTotal()
