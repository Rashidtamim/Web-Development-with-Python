
#largest number
'''a,b,c = map(int,input("Enter 3 numbers ").split())
print(f"{a},{b},{c}")

if a>b and a>c:
    print(f"largest :{a}")
elif b>a and b>c:
    print(f"largest :{b}")
else:
    print(f"largest:{c}")
'''

#simple login system

user = input("Input user name :")
password = int(input("Enter your password :"))
if user == "tamim" and password == 1234:
    print("valid")
else:
    print("invalid")
