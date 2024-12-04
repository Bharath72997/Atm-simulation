print("**********WELCOME***********")
balance = 0
def deposit():
    global balance
    amount = int(input("How much would you like to depsoit: "))
    if amount <= 0:
        print("The amount is invalid")
    else:
        balance += amount


def showBalance():
    print("The balance amount is ", balance)

def withdraw():
    global balance
    amount= int(input("how much would you want to withdraw : "))
    if amount > balance:
        print("Insufficient funds")
    elif amount <= 0:
        print("invalid amount")
    else:
        balance -= amount
    

def exit():
    print("Thank you for visiting")


while True:
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    choice = int(input("Enter the choice 1-4: "))
    if choice == 1:
        showBalance()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        exit()
        break
    else:
        print("This is not a valid choice")



    