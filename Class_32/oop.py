class ShoppingCart:
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
print(f"This is the cart of Shuvo - {shuvo.addCart()}")