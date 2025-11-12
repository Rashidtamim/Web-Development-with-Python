#take a list of numbers from the user and create a new list containing only the square of even numbers
list=[]
num = int(input("Enter the size of the list "))
# even_list = []
for i in range(num):
    n= int(input("Enter item into the list "))
    list.append(n)
print(list)

evens = [n for n in list if n % 2 == 0]
squares = [n**2 for n in evens]
print(squares)
