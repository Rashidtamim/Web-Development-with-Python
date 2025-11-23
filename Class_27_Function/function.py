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

def greet(name = "No entry student"):
    print(f"Hello {name}")
name = input("Enter the student name ")
greet(name)
greet()


#ojana songkhok argument pass korar jnno
def add (*args):
    print(sum(args))
add(5,10,15)



#ami janina dictionary theke koto gulo value ashbe

def newfunc(**kargs):
    print(kargs)
newfunc(name = "riyad",age = 23, isMarried = False, cgpa = 3.87 , dept = "Cse")









#nested funtion
def outer(): #this is global function
    print("outer function")
    def inner():
        print("Inner function")
    inner()
outer()