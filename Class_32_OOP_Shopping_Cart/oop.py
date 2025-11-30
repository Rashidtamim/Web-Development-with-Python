'''class ShoppingCart:
    def __init__(self,product_title,product_quatity, product_price = 120,product_discount=10):
        self.title = product_title
        self.price = product_price
        self.discount = (product_discount/100)*self.price
        self.quantity = product_quatity
    def addCart(self):
        total_price = (self.price - self.discount)*self.quantity
        return f"Product Name : {self.title} , Total price - {total_price} k"
    

product_title = input ("Enter what you want : ")
product_quatity = int(input("Add quatity : "))
Tamim = ShoppingCart(product_title,product_quatity)
print(f"This is the cart of tamim - {Tamim.addCart()}")


product_title = input ("Enter what you want : ")
product_quatity = int(input("Add quatity : "))
shuvo = ShoppingCart(product_title,product_quatity)
print(f"This is the cart of Shuvo - {shuvo.addCart()}")'''


#Create Student, Book, Employee classes

class Students:
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