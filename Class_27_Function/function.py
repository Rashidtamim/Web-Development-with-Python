# def greetings():
#  print("hello world")

# greetings()

# def sum():
#  print(a+b)

'''def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
num1,num2 = map(int , input("Enter the numbers : ").split())
result1=sum(num1,num2)
result2=sub(num1,num2)
result3 = multi(num1,num2)
result4 = div(num1,num2)
print(f"sum = {result1} , subtraction = {result2} , multiplication = {result3} , division = {result4}")
'''
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# multiplication table
'''def table(a):
    for i in range(1,11):
        print(f"{a}*{i} = {i*a}")

a = int(input("Enter the namta : "))
table(a)'''



#Calculator

'''def calculator(a,b,operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b


n1, n2 = map (int,input("Enter the number : ").split())
operator = input("Enter the operation : ")
result = calculator(n1,n2,operator)
print(result)'''

'''def greet(name = "No entry student"):
    print(f"Hello {name}")
name = input("Enter the student name ")
greet(name)
greet()


#ojana songkhok argument pass korar jnno
def add (*args):
    print(sum(args))
add(5,10,15)
'''


#ami janina dictionary theke koto gulo value ashbe

'''def newfunc(**kargs):
    print(kargs)
newfunc(name = "riyad",age = 23, isMarried = False, cgpa = 3.87 , dept = "Cse")'''



# a1 = int(input("Enter a number : "))
# b2 = int(input("Enter 2nd number : "))

'''a1,b2 = map(int,input("Enter two values").split())
print(a1 + b2)'''
#Create a function that prints your name


def func(name):
    print(name)
func("tamim")



#Write a function that takes two numbers and prints the sum.

'''def func(n1,n2):
    return n1 + n2
a,b = map(int,input("Enter two number : ").split())
result = func(a,b)
print(result)
'''
#Create a function with default parameters.
'''def func1(name = "Student"):
    print(f"Hello {name}")
name = input("enter your name")
func1(name)'''

#Write a function that returns the largest of three numbers.

'''def largest(a,b,c):
    if a>b:
        if a > c:
            print(a)
    elif b>a:
        if b>c:
            print(b)
    else:
        print(c)
n1,n2,n3 = map(int,input("Enter three number").split())
largest(n1,n2,n3)'''





#Use *args to add all numbers passed.
def add(*args):
    print(sum(args))

add(1,2,3,4,5)


#Create a function that returns both sum and average.

def suav(a,b):
    print(f" Sum of all numbers : {a+b}  and Average is {(a+b)/2} , multiplication {a*b} , Division {a/b} , integar division {a//b}")
suav(10,23)

#Use **kwargs to print student details.

def student(**kwargs):
    print(kwargs)
student(name = "Tamim" ,age = 26 , Type = "opener" , Avg = 34.5)


#Write a lambda that squares, cubes, and doubles numbers.
square = lambda x : x**2
cubes = lambda x : x**3
double = lambda x : x*2

print(square(5))
print(cubes(5))
print(double(5))

















#nested funtion
'''def outer(): #this is global function
    print("outer function")
    def inner():
        print("Inner function")
    inner()
outer()'''