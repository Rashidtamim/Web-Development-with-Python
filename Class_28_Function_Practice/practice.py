#Create a function that prints your name

'''
def func(name):
    print(name)
a = input("enter your name : ")
func(a)
'''


#Write a function that takes two numbers and prints the sum.

'''def func(n1,n2):
    return n1 + n2
a,b = map(int,input("Enter two number : ").split())
result = func(a,b)
print(result)'''

#Create a function with default parameters.
'''def func1(name = "Student"):
    print(f"Hello {name}")
name = input("enter your name")
func1(name)
func1()'''

#Write a function that returns the largest of three numbers.

'''def largest(a,b,c):
    # print(a,b,c)
    if a>b:
        if a > c:
         print(a)
    elif b>a:
        if b>c:
         print(b)
    else:
        print(c)
n1,n2,n3 = map(int,input("Enter three number : ").split())
largest(n1,n2,n3)'''


# def largest(a, b, c):
#     if a > b and a > c:
#         print(a)
#     elif b > a and b > c:
#         print(b)
#     else:
#         print(c)

# n1, n2, n3 = map(int, input("Enter three numbers: ").split())
# largest(n1, n2, n3)





#Use *args to add all numbers passed.
'''def add(*args):
    print(sum(args))

add(1,2,3,4,5)'''


#Create a function that returns both sum and average.
'''
def suav(a,b):
    print(f" Sum of all numbers : {a+b}  and Average is {(a+b)/2} , multiplication {a*b} , Division {a/b} , integar division {a//b}")
suav(10,23)'''

#Use **kwargs to print student details.

'''def student(**kwargs):
    print(kwargs)
student(name = "Tamim" ,age = 26 , Type = "opener" , Avg = 34.5)'''


#Write a lambda that squares, cubes, and doubles numbers.
'''square = lambda x : x**2
cubes = lambda x : x**3
double = lambda x : x*2
a = int(input("Enter the number : "))
print(square(a))
print(cubes(a))
print(double(a))'''


# square = lambda a : a * a
# print(square(5))
#def square(a): #square = lambda #parameter:

#check a fibonacci 
def fibonacci(a,b,num1):
    for i in range(1,num1+1):
        c = a + b
        a=b
        b=c
    
    
    print(c)


num1 = int(input("Enter the number : "))

fibonacci(0,1,num1)