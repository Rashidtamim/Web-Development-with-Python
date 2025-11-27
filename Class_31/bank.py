print("Welcome to Touch and love Bank")
class Banking:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self,deposit_amount):
        if deposit_amount >= 500:
            self.balance += deposit_amount
            return self.balance
        else:
            print("You have to deposit atleast 500")
    def withdraw(self,withdraw_amount):
        if self.balance > 0:
            if self.balance>=withdraw_amount:
                self.balance -= withdraw_amount
                return self.balance
            else:
                print("Your request balnance is higher than your current balance")
        else:
            print("You dont have sufficient balance")


    def __str__(self):
        return f"Hello MR {self.name} . Your current balance is {self.balance}"
    
input1 = input("Enter your name : ")
initial_amount = int(input("Enter the initial balance : "))
bank1 = Banking(input1,initial_amount)
print(bank1)


deposit_amount = 0
while deposit_amount <500:
    deposit_amount = int(input("Enter Your amount"))
    if deposit_amount>500:
        break
    print("Please deposit atleast 500")
# deposit_amount = int(input("Enter the deposit amount : "))
bank1.deposit(deposit_amount)
print(bank1)

withdraw_amount = int(input("Enter your withdraw amount : "))
bank1.withdraw(withdraw_amount)
print(bank1)
