#student record
class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    # def display_info(self):
    def __str__(self):
        return f"His name is {self.name} and his age is {self.age} and his grade is {self.grade}"
s1 = student("tamim",23,"A+")
print(s1)
# s1.display_info()

#rectangular area and perimeter

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        print(f"{self.length*self.width} cm")
    def perimeter(self):
        print(f"{2*(self.length+self.width)} cm")
s1 = Rectangle(23,45)

s1.area()
s1.perimeter()

#car class
class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model
        self.speed = 0
    def accelarate(self,amount):
        self.speed +=amount
        print(f"Accelated now speed is {self.speed} kmph")
    def brake(self,amount):
        self.speed = max(0,self.speed - amount)
        print(f"Braked speed is now {self.speed} kmph")
    def speed1(self):
        print(f"Current speed is {self.speed} kmph")
c1 = Car("Axio","Toyota")
c1.accelarate(50)
c1.accelarate(30)
c1.brake(20)
c1.speed1()


#Simple bank account
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
    
    def check_balance(self):
        print(f"Balance: ${self.balance}")
        return self.balance

# Test
acc = BankAccount("Emma")
acc.deposit(1000)
acc.withdraw(300)
acc.check_balance()    # Balance: $700
acc.withdraw(800)      # Insufficient funds!








#dog classs
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        print("Woof woof!")
    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday! {self.name} is now {self.age} years old")
    
    def info(self):
        print(f"{self.name} is a {self.age}-year-old {self.breed}")

# Test
dog = Dog("Max", 3, "Golden Retriever")
dog.bark()
dog.birthday()
dog.info()