
'''size = input("Enter the size of the list : ")

list=[]
for i in range(len(size)):
    n = int(input())
    
    if n % 2 == 0:
    
     list.append(list[i]**2)
     
    # list.append(i)
    
print(list)
# evens = [n for n in list if n % 2 == 0]
# squares = [n**2 for n in evens]
# print(squares)
'''

#2.Given a list of integers ,seperate even and odd numbers

'''size = int(input("Enter the size : "))
list = []
even = []
odd = []
for i in range(size):
   n = int(input("Enter the items "))
   list.append(n)
print(list)

for i in list:
   if i % 2 == 0 :
      even.append(i)
   else:
      odd.append(i)

print(even)
print(odd)
'''


#3.

#4.Remove all the duplicate values from a list while maintaing the orginal order

'''size = int (input("Enter the size of the list"))
list = []
for i in range(size):
   list.append
'''


'''1
new = [1,23,34,45,56]
new_Even = []
for index in range (len(new)):
   if new[index]%2 == 0:
      new_Even.append(new[index]**2)
print(new_Even)'''


#2.
'''fruits = ["apple","banana","grape"]
for i in fruits:
   print(i)'''

'''numList = [1,5,67,78,84]
sum = 0
for i in numList:
    sum = sum + i
print(sum)'''



#4 remove all duplicate
'''user_input = list(map(int,input("Enter the size of the list").split()))
lst = []

for i in range(len(user_input)):
    lst.append(i)
print()'''





'''nameList = ["rajulur rashid",'shuvo hossen',"samad islam"]
print(nameList)
nameList1=[]

for i in nameList:
    nameList1.append(i.title())
print(nameList1)
'''


'''newList = [1,5,9,13,6,8,15,20,23,35,49]
newNum =[]
for num in newList:
    if num % 5 != 0:
        continue
    newNum.append(num)

print(newNum)

newList1 = []
for num in newList:
    newList1.append(num)
    if num == 20:
        break
print(newList1)

'''

list = ['Asif',"Uday",'Shuvo','Rajulur Rashid','tamim']

for name in list:
    
    if name == "Rajulur Rashid":
     print(list)
     break

    











# loop 1 to 100
# num % 3 == 0 and num % 5 == 0 ------->print(Fizzbuzz)
# num % 3 == 0 ->print(fizz)
# num % 5 == 0 ->print 




'''for num in range (1,101):
    if num % 3 == 0 and num % 5 == 0: #if num % 15 == 0
    
        print(f"{num} ->Fizzbuzz")
    elif  num % 3 == 0 :
        
        print(f"{num} -> Fizz")
    elif num % 5 == 0:
        print(f"{num} ->Buzz")
    else:
        print(num)'''

    








