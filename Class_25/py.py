# students = {
#     'student1': {
#         'Name': 'Rajulur',    # Fixed the extra space bug (was 'Name ')
#         'age': 24
#     },
#     'student2': {
#         'Name': 'Rashid',
#         'age': 25
#     },
#     'student3': {
#         'Name': 'Tamim',
#         'age': 26
#     },
#     'student4': {
#         'Name': 'Rashid Tamim',
#         'age': 27
#     },
#     'student5': {
#         'Name': 'RRTamim',
#         'age': 28
#     }
# }
# students['student5'].update({
#     "Name":"Shoiko",
#     "Age":29
# })

# students.update({
#     "student6": {
#         "Name": "Shuvo",
#         "Roll": 34
#     }
# }
# )
# print(f"after updating{students}")
# students["student6"].pop("Name")

# students.popitem()
# print(f"After deleting student 6 name :{students}")

# employe = {
#     "Tamim" : {
#         "Subject": "English",
#         "Marks": 65
#     },
#     "Shuvo" : {
#        "Subject" : "Math",
#        "Marks" : 78

#     }
# }
# print(employe)
# del students['student1']
# print(students)


# num1,num2 = map(int,input("Enter any number ").split())
# print(num1,num2)

'''person = dict(name = "Tamim", age = 23)
print(person)
print(person.get("name"))


text = "programming"

count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1   #count er moddhe first e p ashbe 

print(count)'''


#Create a dictionary of 5 students with name and age.

students = {
    "student1":{
        "Name" : "Touch",
        "Age" : "2y"
    },
    "student2":{
        "Name" : "and",
        "Age" : "3y"
    },
    "student3":{
        "Name" : "Solve",
        "Age" : "4y"
    },
    "student4":{
        "Name" : "Software",
        "Age" : "5y"
    },
    "student5":{
        "Name" : "Firm",
        "Age" : "6y"
    }
}

for key in students:   # here we are printing keys of the students
    print(key)
for values in students.values():  #here we are printing the value of the students12345 keys
    print(values)
for values in students:      #both are same for printing the values
    print(students[values])


for key,value in students.items():
    print(key,value)


#change the value of any keys i want to change student5's name in touch and solve
students["student5"]["Name"]="Touch and solve"
#or we can use update function
students["student1"].update(Name="Metro_Firm")
print(students)


#Use update() to add multiple new fields.

students.update({
    'student6' : {
       "Name" : "sium",
       "age":23
    },
    'student7' : {
       "Name" : "aiyub",
       "age":25
    }
})


# print(students)


#Remove 2 items using pop() and del
students.pop("student7")

students.popitem()  #this remove last item
print(students)


del students["student5"]

print(students)


#Create a nested dictionary and access nested values.


employee = {
    'Name' : {
        'Tamim' : "Mirpur",
        'code' : 1216
    }
}
print(employee["Name"]["Tamim"])
print(employee["Name"]["code"])
# print(employee)



#Count character frequency using a dictionary.

text = 'Programming'
count = {}
for i in text:
    if i in count:
        count[i] +=1
    else:
        count[i]=1
print(count)


#Write a program that stores employee details and retrieves them by user input ID.
students = {
    "student1":{
        "Name" : "Touch",
        "Age" : "2y"
    },
    "student2":{
        "Name" : "and",
        "Age" : "3y"
    },
    "student3":{
        "Name" : "Solve",
        "Age" : "4y"
    },
    "student4":{
        "Name" : "Software",
        "Age" : "5y"
    },
    "student5":{
        "Name" : "Firm",
        "Age" : "6y"
    }
}
while True:
    take_input = input("Enter the student name : ").strip()
    print(take_input)
    if take_input == 'quit':
        print("Good Bye")
        break
    if take_input in students:
        info =students[take_input]
        print("Student details ")
        print(info)

    else:
        print("Employee id not found")







