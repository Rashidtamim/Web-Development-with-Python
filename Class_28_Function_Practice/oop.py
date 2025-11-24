class Car:
    color = "black"
    brand = "Tesla"             #whatever we write inside the car this all will be object and this is called as a blueprint
    model = "premio"
    manufactured = 2016
    def __init__(self, c="Yellow",b ="Audi",m = "Q7"):
        self.color=c
        self.brand=b
        self.model=b
    def __str__(self):
        return f"{self.color} {self.brand} {self.model}"


car1 = Car()
car2 = Car()
# car1.color = "White"
# car1.brand = "Axio"
# car1.model = "Rickshay Tesla"
print(car1)
print(car2)