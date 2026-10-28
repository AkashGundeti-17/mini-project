
class Account:
    def __init__(self, account_no, name, phone, balance):
        self.account_no = account_no
        self.name = name
        self.phone = phone
        self.balance = balance


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        account_no = input("Enter Account Number: ")

        for acc in self.accounts:
            if acc.account_no == account_no:
                print("Account number already exists!")
                return

        name = input("Enter Customer Name: ")
        phone = input("Enter Phone Number: ")
        balance = float(input("Enter Initial Balance: "))

        acc = Account(account_no, name, phone, balance)
        self.accounts.append(acc)

        print("Account created successfully!")

    def search_account(self, account_no):
        for acc in self.accounts:
            if acc.account_no == account_no:
                return acc
        return None

    def deposit(self):
        account_no = input("Enter Account Number: ")
        acc = self.search_account(account_no)

        if acc:
            amount = float(input("Enter Deposit Amount: "))

            if amount > 0:
                acc.balance += amount
                print("Amount deposited successfully!")
                print("Current Balance:", acc.balance)
            else:
                print("Enter a valid amount.")
        else:
            print("Account not found!")

    def withdraw(self):
        account_no = input("Enter Account Number: ")
        acc = self.search_account(account_no)

        if acc:
            amount = float(input("Enter Withdrawal Amount: "))

            if amount <= 0:
                print("Enter a valid amount.")
            elif acc.balance >= amount:
                acc.balance -= amount
                print("Withdrawal successful!")
                print("Remaining Balance:", acc.balance)
            else:
                print("Insufficient Balance!")
        else:
            print("Account not found!")

    def check_balance(self):
        account_no = input("Enter Account Number: ")
        acc = self.search_account(account_no)

        if acc:
            print("Account Holder:", acc.name)
            print("Current Balance:", acc.balance)
        else:
            print("Account not found!")

    def remove_account(self):
        account_no = input("Enter Account Number: ")
        acc = self.search_account(account_no)

        if acc:
            self.accounts.remove(acc)
            print("Account removed successfully!")
        else:
            print("Account not found!")

    def update_account(self):
        account_no = input("Enter Account Number: ")
        acc = self.search_account(account_no)

        if acc:
            print("1. Update Name")
            print("2. Update Phone Number")

            choice = input("Enter your choice: ")

            if choice == "1":
                acc.name = input("Enter New Name: ")
                print("Name updated successfully!")
            elif choice == "2":
                acc.phone = input("Enter New Phone Number: ")
                print("Phone number updated successfully!")
            else:
                print("Invalid choice!")
        else:
            print("Account not found!")

    def show_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return

        for acc in self.accounts:
            print("\n--------------------")
            print("Account Number:", acc.account_no)
            print("Name:", acc.name)
            print("Phone:", acc.phone)
            print("Balance:", acc.balance)


bank = Bank()

while True:
    print("\n===== BANK ACCOUNT MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Search Account")
    print("6. Update Account")
    print("7. Remove Account")
    print("8. Show All Accounts")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bank.create_account()

    elif choice == "2":
        bank.deposit()

    elif choice == "3":
        bank.withdraw()

    elif choice == "4":
        bank.check_balance()

    elif choice == "5":
        account_no = input("Enter Account Number: ")
        acc = bank.search_account(account_no)

        if acc:
            print("Account Number:", acc.account_no)
            print("Name:", acc.name)
            print("Phone:", acc.phone)
            print("Balance:", acc.balance)
        else:
            print("Account not found!")

    elif choice == "6":
        bank.update_account()

    elif choice == "7":
        bank.remove_account()

    elif choice == "8":
        bank.show_accounts()

    elif choice == "9":
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice! Please try again.")
