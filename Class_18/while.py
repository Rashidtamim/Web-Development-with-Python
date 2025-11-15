# n = int(input("Enter the number "))
# i = 1
# while i <= 10:
#     print(f"{i} * {n} = {i*n}")
#     i = i + 1


'''
#Using a reversed() function and for loop
list1 = [10,20,30,40,50]
# reverse list
new_list = int(reversed(list1))
# iterate reversed list
for item in new_list:
    print(item) '''



#sum of first n natural numbers
#Goal : take input n , and calculate  the sum of 1 to n using while 
'''n = int(input("Enter the  number "))
i=1
sum = 0
while i <= n:
    sum = sum+i
    i+=1


print("Summation is ",sum)
'''


#armstrong 
# n = int(input("Take a any number to check"))



#print even numbers between 1 and 50
#Goal : use a while loop to print all even numbers from 1 to 50
'''i  = 0
while i <=50:
    print(i)
    i+=2'''
    

list=[]
start = 1
while start<= 50:
    if start % 2 == 0:
        list.append(start)
        # print(list)
    start +=1
print(list)



    






#count digits of a number
#Goal : find how many digits a number has a using while 


'''userInput = int(input("Enter any number"))
rem = 1
count = 0
while rem < 3:
    temp = userInput % 10
    userInput = temp
    print(temp)
    count +=1
    print(count)
    rem+=1

print(count) '''

'''
number = int(input("Enter a positive number (or 0): "))
count = 0
temp = number

# Use while loop and % 10 to extract each digit
while temp > 0:
    digit = temp % 10      # Get last digit
    count = count + 1      # Count it
    temp = temp // 10      # Remove last digit

# Handle case when number is 0 → count is still 0
while count == 0:
    count = 1              # 0 has 1 digit

print("The number has", count, "digit(s).")'''


'''cars=['axio','premio','corolla','aqua']
color = ['grey','black','maron','green']
for i in cars:
    car = cars[i]
    print(car)
    for j in color:
      col=color[j]
      print(col)'''
cars = ['axio', 'premio', 'corolla', 'aqua']
color = ['grey', 'black', 'maron', 'green']

# Store pairs to control output

'''for i in range(len(cars)):
    print(f"{cars[i] } = {color[i]}") 
    i+=1'''
    
    # for j in range(len(color)):
        # col = color[i]
        # print(f" This is car {car} and this is the cars color {col}")


# fruits = ["apple", "banana", "apple"]
# print(fruits.index("banana"))  # 1
# print(fruits.count("apple"))


text = "Python is fun and Python is powerful "
words = text.split()
print(words)

unique_words = list(set(words))
print(unique_words)

