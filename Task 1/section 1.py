# SECTION 1 - SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# Refactored from messy BankAccount
# BankAccount
# Responsibility: Account operations only

class BankAccount:

    def __init__(self, account_number, name, age, balance, account_type):
        self.account_number = account_number
        self.name = name
        self.age = age
        self.balance = balance
        self.account_type = account_type
        self.status = "Active"
        self.pin = None
        self.transaction_log = []

    def deposit(self, amount):

        if self.status != "Active":
            print("Account is not active")
            return False

        if amount <= 0:
            print("Invalid deposit amount")
            return False

        self.balance += amount

        self.transaction_log.append(
            f"DEPOSIT: Rs. {amount} | New balance: {self.balance}"
        )

        return True

    def withdraw(self, amount, entered_pin=None):

        if self.status != "Active":
            print("Account is not active")
            return False

        if self.pin is not None:
            if entered_pin is None or entered_pin != self.pin:
                print("Incorrect PIN")
                return False

        if amount <= 0:
            print("Invalid withdrawal amount")
            return False

        minimum_balance = (
            500.0 if self.account_type == "Savings" else 1000.0
        )

        if self.balance - amount < minimum_balance:
            print("Withdrawal would breach minimum balance")
            return False

        self.balance -= amount

        self.transaction_log.append(
            f"WITHDRAW: Rs. {amount} | New balance: {self.balance}"
        )

        return True

    def close_account(self):

        if self.status == "Inactive":
            return False

        self.status = "Inactive"
        return True

    def reopen_account(self):

        if self.status == "Active":
            return False

        self.status = "Active"
        return True

    def set_pin(self, new_pin):

        if 1000 <= new_pin <= 9999:
            self.pin = new_pin
            return True

        return False

    def verify_pin(self, entered_pin):

        return self.pin is not None and self.pin == entered_pin

# AccountRepository
# Responsibility: Database persistence

class AccountRepository:

    def save(self, account):

        print(
            f"[DB] Saving account "
            f"{account.account_number} to MySQL..."
        )

# NotificationService
# Responsibility: Sending notifications

class NotificationService:

    def send(self, message):

        print(
            f"[EMAIL] To: Account Holder | {message}"
        )

# StatementGenerator
# Responsibility: Generating account statement

class StatementGenerator:

    def generate(self, account):

        print(
            f"---- Statement for Account "
            f"#{account.account_number} ({account.name}) ----"
        )

        for entry in account.transaction_log:
            print(entry)

        print(f"Current Balance: Rs. {account.balance}")

        print(
            "-----------------------------------------------------"
        )

# Main

if __name__ == "__main__":

    account = BankAccount(
        "ACC1001",
        "Ajay",
        20,
        5000,
        "Savings"
    )

    repository = AccountRepository()
    notification = NotificationService()
    statement = StatementGenerator()

    account.deposit(1000)

    notification.send(
        "Your deposit of Rs. 1000 was successful."
    )

    repository.save(account)

    account.withdraw(500)

    notification.send(
        "Your withdrawal of Rs. 500 was successful."
    )

    repository.save(account)

    statement.generate(account)