# BankAccount class definition
class BankAccount:
    def __init__(self, name, balance=0):
        """
        Initialize the BankAccount with account holder's name and an optional balance.
        :param name: str - Name of the account holder
        :param balance: float or int - Initial balance (default is 0)
        """
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        :param amount: float or int - Amount to deposit
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient balance exists.
        :param amount: float or int - Amount to withdraw
        """
        if amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"Current balance: {self.balance}")

# Example usage:
account = BankAccount("Alice")
account.deposit(100)
account.withdraw(50)
account.check_balance()