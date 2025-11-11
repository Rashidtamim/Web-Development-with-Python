#Given a list of integers ,separate even and odd numbers into two different list:
list=[]
even_list=[]
odd_list=[]
num = int(input("Enter the size of the list "))
# even_list = []
for i in range(num):
    n= int(input("Enter item into the list "))
    list.append(n)
print(list)

# evens = [n for n in list if n % 2 == 0]
# print(evens)

for n in list:
    if n%2==0 :
        even_list.append(n)
    else:
        odd_list.append(n)
print("Even number list",even_list)
print("Odd number list ",odd_list)
