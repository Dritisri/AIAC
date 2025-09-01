# BankAccount class implementation

class BankAccount:
    def __init__(self, name, balance=0):
        """
        Initialize the BankAccount with account holder's name and an optional balance (default is 0).
        """
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient balance exists.
        Otherwise, display an error message.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"Current balance: {self.balance}")

# Example usage:
if __name__ == "__main__":
    # Create a new bank account for John with an initial balance of 100
    account = BankAccount("John", 100)
    account.check_balance()      # Should display 100
    account.deposit(50)          # Should add 50 to balance
    account.withdraw(30)         # Should subtract 30 from balance
    account.withdraw(200)        # Should show error (insufficient balance)
    account.check_balance()      # Should display the updated balance

"""
Explanation:

1. The BankAccount class is defined with two attributes: 'name' (account holder's name) and 'balance' (default is 0).
2. The __init__ method initializes these attributes when a new object is created.
3. The deposit(amount) method adds the specified amount to the balance if the amount is positive.
4. The withdraw(amount) method checks if the withdrawal amount is positive and if there is enough balance.
   - If so, it deducts the amount from the balance.
   - If not, it prints an error message.
5. The check_balance() method prints the current balance.
6. Example usage demonstrates creating an account, depositing, withdrawing, and checking the balance.
"""
