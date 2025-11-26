class Animal:
    Cat = "SweetCat"
    Dog = "Kutta"
    Tiger = "Sheru"
animal = Animal()
print(animal.Cat)
print(animal.Dog)
print(animal.Tiger)


class Animal1:
    def __init__(self,name = "Tamim",color = "Black",breed = "Cat"):
        self.sojib = name
        self.color = color
        self.breed = breed
    
    def show(self):
        print( f"The name is {self.sojib}, The color is {self.color} ,The breed is {self.breed}")

# n1,n2,n3 = map(str,input("Enter the attribute value : ").split())
# name = input("ENter the name ")
# color = input("Enter the color ")
# breed = input("Enter the breed")
# animal2 = Animal1(name,color,breed)
# print(animal)
animal2 = Animal1()
animal2.show()
