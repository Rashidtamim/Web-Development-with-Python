print("Welcome to bKash")
print("1.Send Money")
print("2.Cashout")
print("3.My bKash")
print("4.Exit")

option = int(input("Enter your desire oprion(eg:1,2...): " ))
balance = 4000
count = 0

while option != 4:
    if option == 1:
        mobile = int(input("Enter bKash number: "))
        send_amount = int(input("Enter send amount: "))
        if(balance > send_amount):
            balance -= send_amount
        else:
            print("Insufficient balance!")
        
        
    elif option == 3:
        print(f"Balance: {balance}")
        
    elif option == 2:
        withdraw = int(input("Enter amount: "))
        balance -= withdraw
        
    count+=1
    if count > 0:
        print("1.Send Money")
        print("2.Cashout")
        print("3.My bKash")
        print("4.Exit")
        
    option = int(input("Enter option: "))