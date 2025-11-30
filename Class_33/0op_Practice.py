#Create Student, Book, Employee classes

'''class Students:
    def __init__(self,name="Tamim",section="b",roll =1):
        self.name = name
        self.section = section
        self.roll = roll
    def __str__(self):
        return f"Name is : {self.name} , Section is {self.section} , And roll is {self.roll}"
class Book:
    def __init__(self,Book_name,author):
        self.Book_name = Book_name
        self.author = author
    def __str__(self):
        return f"Book name is {self.Book_name} , Author name is {self.Book_name}"
class Employee:
    def __init__(self,Emp_name,Emp_id):
        self.Emp_name = Emp_name
        self.Emp_id = Emp_id
    def __str__(self):
        return f"Employee name is {self.Emp_name}"
a1 = Students('Rashid',"c",1)
a2 = Book('Alone',"RRTamim")
a3 = Employee('Rajulur',1)
print(a1)
print(a2)
print(a3)
'''
#Build a Calculator class
class Calculator:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def calculate(self):
     if self.c == '+' :
        return self.a + self.b
     elif self.c == '-':
        return self.a - self.c
     elif self.c == '*':
        return self.a * self.b
     elif self.c == '/':
        return self.a / self.b
          
    #     def add(self):
    #     return f"{self.a + self.b}"
    # def sub(self):
    #     return f"{self.a - self.b}"
    # def mul(self):
    #     return f"{self.a * self.b}"
    # def div(self):
    #     return f"{self.a / self.b}"
    

operand1 = int(input("Enter the operand 1 : "))
operand2 = int(input("Enter the operand 2 : "))
operator = input("Enter the operator : ")
    
a = Calculator(operand1,operand2,operator)
print(a.add())