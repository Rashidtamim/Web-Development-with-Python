#1Create a dictionary of 5 students with name and age
students ={
    'student1':{
        'Name ' : 'Rajulur',
        'age' : 24 
    },

    'student2' : {
        'Name ' : 'Rashid',
        'age' : 25 
    },

    'student3' : {
        'Name ' : 'Tamim',
        'age' : 26 
    },

    'student4' : {
        'Name ' : 'Rashid Tamim',
        'age' : 27
    },

    'student5' : {
        'Name ' : 'RRTamim',
        'age' : 28
    },
}
# print(students['student1']['Name '])

print(students)



#2 Print all keys and values using loops.

for i in students.values():
    print(f" key means name is {i['Name ']} and the age is {i['age']} ")
   


    

#3 Change the value of any key.
'''student1 = {
        'Name' : 'Rajulur',
        'age' : 24 
    }
student1['Name'] = 'Tamim'
print(student1)'''


#4 Use update() to add multiple new fields.


'''student1 = {
        'Name' : 'Rajulur',
        'age' : 24 
    }

student1.update({
    'grade': 'A',
    'city': 'Dhaka',
    'hobby': 'Cricket',
    'joined_year': 2023
})
print(student1)
'''

#5 Remove 2 items using pop() and del.

'''students ={
    'student1':{
        'Name ' : 'Rajulur',
        'age' : 24 
    },

    'student2' : {
        'Name ' : 'Rashid',
        'age' : 25 
    },

    'student3' : {
        'Name ' : 'Tamim',
        'age' : 26 
    },

    'student4' : {
        'Name ' : 'Rashid Tamim',
        'age' : 27
    },

    'student5' : {
        'Name ' : 'RRTamim',
        'age' : 28
    }
}

First_item = students.pop('student4')
print(First_item)
print(f"After removing student5  {students}")


Second_item = students.pop('student5')
print(Second_item)
print(f"After removing student5  {students}")'''


#6 Create a nested dictionary and access nested values.


'''students ={
    'student1':{
        'Name ' : 'Rajulur',
        'age' : 24 
    },

    'student2' : {
        'Name ' : 'Rashid',
        'age' : 25 
    },

    'student3' : {
        'Name ' : 'Tamim',
        'age' : 26 
    },

    'student4' : {
        'Name ' : 'Rashid Tamim',
        'age' : 27
    },

    'student5' : {
        'Name ' : 'RRTamim',
        'age' : 28
    }
}

print(f"{students['student1']['Name ']} age is  {students['student1']['age']}")
print(f"{students['student2']['Name ']} age is  {students['student2']['age']}")
print(f"{students['student3']['Name ']} age is  {students['student3']['age']}")
print(f"{students['student4']['Name ']} age is  {students['student4']['age']}")
print(f"{students['student5']['Name ']} age is  {students['student5']['age']}")
'''
#7 Count character frequency using a dictionary.
'''text = "programming"

count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)
'''
#8 Convert two lists into a dictionary:
# -- Keys → Names
# -- Values → Marks
'''names = ['Tamim', 'Rashid', 'Shuvo', 'Morshed']
marks = [85, 92, 78, 88]

dict_names =dict(zip(names,marks))
print(dict_names)
'''



#9 Write a program that stores employee details and retrieves them by user input ID.


employees = {
    'E101': {'name': 'Rashid Tamim', 'dept': 'IT', 'salary': 75000, 'city': 'Dhaka'},
    'E102': {'name': 'Rajulur Rashid', 'dept': 'HR', 'salary': 68000, 'city': 'Chittagong'},
    'E103': {'name': 'Shuvo Hossen', 'dept': 'Finance', 'salary': 82000, 'city': 'Dhaka'},
    'E104': {'name': 'Hashem Ali', 'dept': 'Marketing', 'salary': 71000, 'city': 'Sylhet'}
}

while True:
    emp_id = input("Enter Employee ID (or 'quit' to exit): ").strip()
    
    if emp_id.lower() == 'quit':
    
        print("Goodbye!")
        break
    
    if emp_id in employees:
        info = employees[emp_id]
        print("\n--- Employee Details ---")
        print(f"Name    : {info['name']}")
        print(f"Dept    : {info['dept']}")
        print(f"Salary  : {info['salary']}")
        print(f"City    : {info['city']}")
    else:
        print("Employee ID not found!")