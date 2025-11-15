

#Write a program to find the factorial of a number using a for loop
'''num=int(input("enter the number"))
fact = 1
for i in range (num, 0 , -1):
    fact = fact * i
print(fact)'''



'''n = int(input("Enter a factorial number: "))
fact = 1
i = n

while i > 0:
    fact = fact * i
    i -= 1       
print(fact)'''


#1.	Write a program using a while loop to print numbers from 1 to 10.
"""
i = 1

while i <= 10:
    print(i)
    i +=1
    
"""


#2.	Write a program to print all even numbers between 1 and 50 using a for loop.

# i = 1
"""
while i <= 50:
    print(i)
    i +=2"""
    
    
    
"""while i <= 50: 
    if i%2==0:
        print(i)
        
    i +=1
"""
    
   
"""for i in range(1, 51):
    if i % 2 == 0:
        print(i)
    
"""

"""for i in range(2, 51, 2):
    print(i)
"""

#3.	Write a program to calculate the sum of numbers from 1 to 100 using a while loop.

"""sum = 0
i = 1

while i <= 100:
    sum +=i # sum = sum + i
    i+=1
    
print(sum)"""


# 4.	Using a for loop, print each character of a string given by the user.

# user_input = input("enter a string: ")

# for i in user_input:
#     print(i)

# i = 0
"""
while i < len(user_input):
    print(user_input[i])
    i+=1
"""

# 5.	Write a program that prints the multiplication table of a number using a for loop.


# Task

#6.	Write a program to reverse a number using a while loop.

'''temp = int(input("Enter a number: "))
reverser_number = 0


while temp != 0:
    rem = temp % 10 # 123 > 3 > 2 > 1
    print(rem)
    reverser_number = (reverser_number  * 10) + rem
    print(reverser_number)
    temp = temp // 10 # 12 # 1 
    print(temp)
    
print(reverser_number)'''
"""
count = 0
user_number = int(input("Enter a number: "))

temp = user_number

while temp !=0:
    temp = temp // 10
    count +=1
print(count)

"""

#9.	Write a program to find the factorial of a number using a for loop.

'''num = int(input("Enter a number: "))

fact = 1

for i in range(num, 0, -1):
    fact = fact * i'''



#1.	Write a program using a while loop to print numbers from 1 to 10.
'''i = 1
while i <= 10:
    print(i)
    i +=1'''
    
    
#Write a program to print all even numbers between 1 and 50 using a for loop.
'''i = 1
while i <=50:
    if i % 2 == 0:
     print(i)
    i+=1'''
'''i=2
while i <= 50:
   print(i)
   i+=2'''

'''for i in range(2,51,2):
   print(i)'''

#3.	Write a program to calculate the sum of numbers from 1 to 100 using a while loop.
'''i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i+=1
print(sum)'''
'''
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)
'''


# 4.	Using a for loop, print each character of a string given by the user.

'''i = 0
user_input = input("Enter the String")
while i <len(user_input):
    print(user_input[i])
    i +=1'''


'''user_input = input("Enter the number : ")
for i in user_input:
    print(i)
'''

# 5.	Write a program that prints the multiplication table of a number using a for loop.

'''tab_of_number=int(input("Enter "))
# for i in range(1,11):
#     print(f"{i} * {tab_of_number} = {i*tab_of_number}")
i = 1
while i <= 10:
    print(f"{i} * {tab_of_number} = {i*tab_of_number}")
    i+=1'''

#9.	Write a program to find the factorial of a number using a for loop.

'''factorial_number = int(input("Enter the facatorial number : "))
fact = 1
for i in range(factorial_number,0,-1):
    
    fact = fact * i

print(fact)'''

'''factorial_number = int(input("Enter the factorial number : "))
fact = 1
i = 5
while i > 0:
    fact = fact * i
    i-=1
print(fact)
'''
'''
i =1
for i in range(1,6):
    for j in range(1,6):
        print("*" , end=' ')
    print()'''