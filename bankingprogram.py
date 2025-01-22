


# def show_balance():
#     print(f"Your balance is ${balance:.2f}")

# def deposit ():
#     amount = float (input ("Enter amount to be deposited: "))

#     if amount < 0:
#         print ("Amount not valid!")
#     else:
#         return amount

# def withdraw ():
#     amount = float (input ("Enter amount to be withdrawn: "))
#     if amount > balance:
#         print ("Insufficiet funds!")
#     elif amount < 0:
#         print ("Amount must be greater than 0")
#     else:
#         return amount
# balance = 0
# is_running = True

# while is_running:

#     print ("Banking Program")
#     print ("1. Show balance")
#     print ("2. Deposit")
#     print ("3. Withdraw")
#     print ("4. Exit")

#     choice = input ("Enter your choice (1-4):")

#     if choice == "1":
#         show_balance ()
#     elif choice == "2":
#         balance += deposit()
#     elif choice == "3":
#         balance -= withdraw()
#     elif choice == "4":
#         is_running = False
#     else:
#         print ("Invalid Choice")

# print ("Thank you! Have a nice day")



def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to be deposited: "))

    if amount < 0:
        print("Amount not valid!")
        return 0  # Return 0 if deposit is invalid
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds!")
        return 0  # Return 0 if withdrawal is not possible
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0  # Return 0 if withdrawal is invalid
    else:
        return amount

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance(balance)
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw(balance)
    elif choice == "4":
        is_running = False
    else:
        print("Invalid Choice")

print("Thank you! Have a nice day!")
