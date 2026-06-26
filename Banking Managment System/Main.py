from bank import Bank
from File_Manager import FileManager

bank = Bank()
file_manager = FileManager()

# Load saved accounts when the program starts
bank.accounts = file_manager.load_accounts()

while True:

    print("BANKING MANAGEMENT SYSTEM")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View All Accounts")
    print("5. Delete Account")
    print("6. Save Accounts")
    print("7. Load Accounts")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        account_name = input("Enter account name: ")
        name = input("Enter customer name: ")
        balance = float(input("Enter starting balance: "))

        bank.create_account(account_name, name, balance)

    elif choice == "2":

        account_name = input("Enter account name: ")
        amount = float(input("Enter deposit amount: "))

        bank.deposit_money(account_name, amount)

    elif choice == "3":

        account_name = input("Enter account name: ")
        amount = float(input("Enter withdrawal amount: "))

        bank.withdraw_money(account_name, amount)

    elif choice == "4":

        bank.display_accounts()

    elif choice == "5":

        account_name = input("Enter account name: ")

        bank.remove_account(account_name)

    elif choice == "6":

        file_manager.save_accounts(bank.accounts)

    elif choice == "7":

        bank.accounts = file_manager.load_accounts()
        print("Accounts loaded successfully.")

    elif choice == "8":

        file_manager.save_accounts(bank.accounts)
        print("Thank you for using the Banking Management System.")
        break

    else:

        print("Invalid option. Please try again.")