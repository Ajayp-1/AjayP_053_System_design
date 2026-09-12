# SECTION 3 - LISKOV SUBSTITUTION PRINCIPLE (LSP)
# Part 1 - Rectangle / Square Example

class Rectangle:

    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

def calculate_area(rectangle):

    rectangle.set_width(20)
    rectangle.set_height(10)

    return rectangle.area()

rectangle = Rectangle()

print(
    "Rectangle area:",
    calculate_area(rectangle)
)

square = Square()

print(
    "Square area:",
    calculate_area(square)
)

# Part 2 - Banking LSP Problem

class Account:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class SavingsAccount(Account):

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(
                f"Savings withdrawal successful: Rs. {amount}"
            )
        else:
            print("Insufficient balance")

class FixedDepositAccount(Account):

    def withdraw(self, amount):

        raise NotImplementedError(
            "Fixed Deposit account does not support withdrawal"
        )

# Demonstrating the LSP violation

accounts = [
    SavingsAccount("S001", 5000),
    FixedDepositAccount("FD001", 10000)
]

for account in accounts:

    try:
        account.withdraw(1000)

    except NotImplementedError as e:
        print("Error:", e)

# LSP FIX
# Withdrawable Interface

class Withdrawable:

    def withdraw(self, amount):
        raise NotImplementedError

# Savings Account

class SavingsAccountFixed(Account, Withdrawable):

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(
                f"Savings withdrawal successful: Rs. {amount}"
            )
        else:
            print("Insufficient balance")

# Current Account

class CurrentAccount(Account, Withdrawable):

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
            print(
                f"Current withdrawal successful: Rs. {amount}"
            )
        else:
            print("Insufficient balance")

# Fixed Deposit Account
# Does NOT implement Withdrawable

class FixedDepositAccountFixed(Account):
    pass

# Use only accounts that are withdrawable

withdrawable_accounts = [
    SavingsAccountFixed("S001", 5000),
    CurrentAccount("C001", 7000)
]

for account in withdrawable_accounts:

    account.withdraw(1000)