"""print('Hello')
print('My name is tamim')
print('') """


#this is the first class of python
'''name= 'Tamim'
age= 25
adress="Uttara ,Dhaka-1216"
Rent=12.7
print(name)
print(type(name))

print(type(age))
print(type(adress))
print(type(Rent))

print(name,type(name))
print(age,type(age))
print(adress,type(adress))
print(Rent,type(Rent))

print(f"name: {type(name)} , age is {age}")

user_name= input("Enter your name ")
age= int(input("Enter your age "))

print(f"YOur name is {user_name}! and your age is {age} years old")'''


'''num1,num2 = map(int,input("Enter two numbers : ").split())
print(num1+num2)
print(num1-num2)
print(num1/num2)
print(num1%num2)
print(num1//num2)'''


age=int(input("Enter your age : "))

if age>= 18:
    print("you are eligible for vote")
    print("okay")
else:
    print("You are not eligible")
print("Bangladesh is not for beginer")

marks=int(input("Enter your marks for the result "))
if marks >= 90:
    print("You got A+")
elif (marks > 80 and marks > 70):
    print("You have got A")
elif (marks> 60 and marks < 70):
    print("You have got A-")
else:
    print("your are fail")