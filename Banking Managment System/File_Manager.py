import csv
from account import account


class FileManager:

    def save_accounts(self, account_list):

        with open("accounts.csv", "w", newline="") as file:

            writer = csv.writer(file)

            # Write the header
            writer.writerow(["Account Name", "Name", "Balance"])

            # Write each account
            for acc in account_list:

                writer.writerow([
                    acc.account_name,
                    acc.name,
                    acc.balance
                ])

        print("Accounts saved successfully.")

    def load_accounts(self):

        account_list = []

        try:

            with open("accounts.csv", "r", newline="") as file:

                reader = csv.reader(file)

                # Skip the header if it exists
                next(reader, None)

                for row in reader:

                    # Ignore empty rows
                    if len(row) == 0:
                        continue

                    new_account = account(
                        row[0],
                        row[1],
                        float(row[2])
                    )

                    account_list.append(new_account)

        except FileNotFoundError:

            print("No saved accounts found.")

        return account_list

    def create_file(self):

        with open("accounts.csv", "a", newline=""):
            pass

    def clear_file(self):

        with open("accounts.csv", "w", newline="") as file:

            writer = csv.writer(file)
            writer.writerow(["Account Name", "Name", "Balance"])

        print("File cleared.")