

#Write a program to find the factorial of a number using a for loop
'''num=int(input("enter the number"))
fact = 1
for i in range (num, 0 , -1):
    fact = fact * i
print(fact)'''



n = int(input("Enter a factorial number: "))
fact = 1
i = n

while i > 0:
    fact = fact * i
    i -= 1       
print(fact)





