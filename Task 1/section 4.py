# SECTION 4 - INTERFACE SEGREGATION PRINCIPLE (ISP)
# DEPENDENCY INVERSION PRINCIPLE (DIP)
# PART 1 - ISP
# Small capability interfaces

class Depositable:

    def deposit(self, amount):
        raise NotImplementedError


class Withdrawable:

    def withdraw(self, amount):
        raise NotImplementedError


class Transferable:

    def transfer(self, amount, account):
        raise NotImplementedError


class StatementProvider:

    def get_statement(self):
        raise NotImplementedError


class LoanEligible:

    def apply_for_loan(self):
        raise NotImplementedError

# ATM
# Implements only the operations it needs

class ATM(Depositable, Withdrawable):

    def deposit(self, amount):

        print(f"ATM deposit: Rs. {amount}")

    def withdraw(self, amount):

        print(f"ATM withdrawal: Rs. {amount}")

# Savings Account
# Implements required capabilities

class SavingsAccount(
    Depositable,
    Withdrawable,
    Transferable,
    StatementProvider
):

    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

        print(
            f"Deposited Rs. {amount}"
        )

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount

            print(
                f"Withdrawn Rs. {amount}"
            )
        else:
            print("Insufficient balance")

    def transfer(self, amount, account):

        if amount <= self.balance:

            self.balance -= amount
            account.balance += amount

            print(
                f"Transferred Rs. {amount}"
            )

        else:
            print("Insufficient balance")

    def get_statement(self):

        print(
            f"Account: {self.account_number}"
        )

        print(
            f"Name: {self.name}"
        )

        print(
            f"Balance: Rs. {self.balance}"
        )

# PART 2 - DIP
# AccountRepository - Abstraction

class AccountRepository:

    def save(self, account):
        raise NotImplementedError

    def load(self, account_number):
        raise NotImplementedError

# MySQL Repository

class MySQLAccountRepository(AccountRepository):

    def save(self, account):

        print(
            f"[MySQL] Saving account "
            f"{account.account_number}"
        )

    def load(self, account_number):

        print(
            f"[MySQL] Loading account {account_number}"
        )

# File Repository
# Reads/writes:
# accountNumber,name,balance

class FileAccountRepository(AccountRepository):

    def __init__(self, filename="accounts.txt"):
        self.filename = filename

    def save(self, account):

        with open(self.filename, "a") as file:

            file.write(
                f"{account.account_number},"
                f"{account.name},"
                f"{account.balance}\n"
            )

        print(
            f"[FILE] Account {account.account_number} saved"
        )

    def load(self, account_number):

        try:

            with open(self.filename, "r") as file:

                for line in file:

                    data = line.strip().split(",")

                    if len(data) == 3:

                        number, name, balance = data

                        if number == account_number:

                            return {
                                "account_number": number,
                                "name": name,
                                "balance": float(balance)
                            }

        except FileNotFoundError:

            print("File not found")

        return None

# Bank
# Depends on AccountRepository abstraction

class Bank:

    def __init__(self, repository):

        self.repository = repository

    def save_account(self, account):

        self.repository.save(account)

    def load_account(self, account_number):

        return self.repository.load(account_number)

# MAIN

if __name__ == "__main__":

    account = SavingsAccount(
        "S001",
        "Ajay",
        5000
    )

    # ISP demonstration
    atm = ATM()

    atm.deposit(1000)
    atm.withdraw(500)

    account.deposit(2000)
    account.withdraw(500)

    account.transfer(
        1000,
        SavingsAccount("S002", "Rahul", 3000)
    )

    account.get_statement()

    # DIP with MySQL
    mysql_repository = MySQLAccountRepository()

    bank = Bank(mysql_repository)

    bank.save_account(account)

    # Switch to File Repository
    # Bank class does not need to be changed

    file_repository = FileAccountRepository(
        "accounts.txt"
    )

    bank = Bank(file_repository)

    bank.save_account(account)

    loaded_account = bank.load_account("S001")

    print(
        "Loaded account:",
        loaded_account
    )