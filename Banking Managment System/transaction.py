class Transaction:

    def __init__(self, account_name, transaction_type, amount):
        self.account_name = account_name
        self.transaction_type = transaction_type
        self.amount = amount

    def display(self):
        print("\n--Transaction ")
        print(f"Account Name: {self.account_name}")
        print(f"Transaction: {self.transaction_type}")
        print(f"Amount: {self.amount}")

    def get_account_name(self):
        return self.account_name

    def get_transaction_type(self):
        return self.transaction_type

    def get_amount(self):
        return self.amount