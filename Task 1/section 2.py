# SECTION 2 - OPEN/CLOSED PRINCIPLE (OCP)
# BankAccount

class BankAccount:

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

# InterestPolicy
# Responsibility: Define interest calculation

class InterestPolicy:

    def calculate(self, balance):
        raise NotImplementedError

# Savings Account - 4%

class SavingsInterestPolicy(InterestPolicy):

    def calculate(self, balance):
        return balance * 0.04

# Current Account - 1%

class CurrentInterestPolicy(InterestPolicy):

    def calculate(self, balance):
        return balance * 0.01

# Salary Account - 5%
# Added without modifying existing policies

class SalaryAccount(BankAccount):
    pass

class SalaryInterestPolicy(InterestPolicy):

    def calculate(self, balance):
        return balance * 0.05

# Interest Calculator

class InterestCalculator:

    def __init__(self, policy):
        self.policy = policy

    def calculate(self, account):

        return self.policy.calculate(account.balance)

# Notification Service

class NotificationService:

    def send(self, message):
        print(f"[NOTIFICATION] {message}")

class EmailNotificationService(NotificationService):

    def send(self, message):
        print(f"[EMAIL] {message}")

class SMSNotificationService(NotificationService):

    def send(self, message):
        print(f"[SMS] {message}")

# Main

if __name__ == "__main__":

    savings = BankAccount(
        "S001",
        "Ajay",
        10000
    )

    current = BankAccount(
        "C001",
        "Rahul",
        10000
    )

    salary = SalaryAccount(
        "SAL001",
        "Arun",
        10000
    )

    savings_calculator = InterestCalculator(
        SavingsInterestPolicy()
    )

    current_calculator = InterestCalculator(
        CurrentInterestPolicy()
    )

    salary_calculator = InterestCalculator(
        SalaryInterestPolicy()
    )

    print(
        "Savings Interest:",
        savings_calculator.calculate(savings)
    )

    print(
        "Current Interest:",
        current_calculator.calculate(current)
    )

    print(
        "Salary Interest:",
        salary_calculator.calculate(salary)
    )

    # Email can be replaced by SMS without changing BankAccount
    notification = EmailNotificationService()
    notification.send("Interest calculated successfully.")

    notification = SMSNotificationService()
    notification.send("Interest calculated successfully.")