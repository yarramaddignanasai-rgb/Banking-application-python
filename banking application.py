class SwissBank:

    IFSC = "SWISS1234"
    Branch_Code = 1
    Location = "Marathahalli"

    def __init__(self, name, acc_no, mob_no, balance, pin):
        self.name = name
        self.acc_no = acc_no
        self.mob_no = mob_no
        self.balance = balance
        self.pin = pin

    # Show details
    def Details(self):
        print("\n----- Account Details -----")
        print(f"Name           : {self.name}")
        print(f"Account Number : {self.acc_no}")
        print(f"Contact Number : {self.mob_no}")
        print(f"IFSC Code      : {SwissBank.IFSC}")
        print(f"Branch Code    : {SwissBank.Branch_Code}")
        print(f"Location       : {SwissBank.Location}")
        print("----------------------------")

    # Check balance with password attempts
    def Check_Bal(self):
        count = 3
        while count != 0:
            print(f"\nNumber of attempts left: {count}")
            if SwissBank.Take_password() == self.pin:
                print(f"Available Balance: ₹{self.balance}")
                print("Transaction Done")
                break
            else:
                print("Invalid PIN")
                count -= 1
        else:
            print("Try again after 24 hours")

    # Deposit money
    def Deposit(self):
        count = 3
        while count != 0:
            print(f"\nNumber of attempts left: {count}")
            if SwissBank.Take_password() == self.pin:
                money = int(input("Enter the amount to deposit: "))
                if 100 <= money <= 40000:
                    if money % 100 == 0:
                        self.balance += money
                        print("Money added successfully!")
                        print("Transaction Done")
                        break
                    else:
                        print("Check the denominations (multiples of 100 only)")
                else:
                    print("Invalid Amount! (100 - 40000 only)")
            else:
                print("Invalid PIN")
                count -= 1
        else:
            print("Try again after 24 hours")

    # Withdraw money
    def Withdraw(self):
        count = 3
        while count != 0:
            print(f"\nNumber of attempts left: {count}")
            if SwissBank.Take_password() == self.pin:
                money = int(input("Enter the amount to withdraw: "))
                if money <= self.balance:
                    if 100 <= money <= 20000:
                        if money % 100 == 0:
                            self.balance -= money
                            print("Amount debited successfully!")
                            print("Transaction Done")
                            break
                        else:
                            print("Check denominations (multiples of 100 only)")
                    else:
                        print("Invalid Amount! (100 - 20000 only)")
                else:
                    print("Insufficient Balance!")
            else:
                print("Invalid PIN")
                count -= 1
        else:
            print("Try again after 24 hours")

    @classmethod
    def Change_Loc(cls, new_location):
        cls.Location = new_location

    @staticmethod
    def Take_password():
        return int(input("Enter 4-digit PIN: "))


# ---------------------------------------
# Create Accounts
# ---------------------------------------
cust1 = SwissBank("Name1", 123456789, 9999999999, 10000, 1111)
cust2 = SwissBank("Name2", 987654321, 8888888888, 40000, 2222)
cust3 = SwissBank("Name3", 9849894949, 7777777777, 20000, 3333)

# ---------------------------------------
# Menu for Customer 1
# ---------------------------------------
while True:
    print("\n===== BANKING MENU =====")
    print("1. Account Details")
    print("2. Check Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        cust1.Details()

    elif ch == "2":
        cust1.Check_Bal()

    elif ch == "3":
        cust1.Deposit()

    elif ch == "4":
        cust1.Withdraw()

    elif ch == "5":
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid Choice!")
