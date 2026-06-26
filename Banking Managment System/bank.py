from account import account

class Bank:

    def __init__(self):
        self.accounts = []

    def create_account(self, account_name, name, balance):
        new_account = account(account_name, name, balance)
        self.accounts.append(new_account)
        print(f"Account '{account_name}' created successfully.")

    def get_account(self, account_name):
        for acc in self.accounts:
            if acc.account_name == account_name:
                return acc

        print(f"Account '{account_name}' not found.")
        return None

    def display_accounts(self):
        if not self.accounts:
            print("No accounts found.")
        else:
            for acc in self.accounts:
                acc.display()

    def remove_account(self, account_name):
        acc = self.get_account(account_name)

        if acc:
            self.accounts.remove(acc)
            print(f"Account '{account_name}' removed successfully.")

    # ← ADD THE NEXT TWO METHODS HERE

    def deposit_money(self, account_name, amount):
        acc = self.get_account(account_name)

        if acc:
            acc.deposit(amount)

    def withdraw_money(self, account_name, amount):
        acc = self.get_account(account_name)

        if acc:
            acc.withdraw(amount)