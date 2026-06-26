class account:

    def __init__(self, account_name, name, balance):
        self.account_name = account_name
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")

    def display(self):
        print(" Account Details")
        print(f"Account Name : {self.account_name}")
        print(f"Customer Name: {self.name}")
        print(f"Balance      : {self.balance}")

    def get_balance(self):
        return self.balance