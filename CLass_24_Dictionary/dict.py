#1 Create a dictionary of 5 students with name and age.


students = {
    'studen1' : {
        'Name1' : "Tamim" ,
        'age' : 24
    },
    'studen2' : {
        'Name2' : "Rashid" ,
        'age' : 25
    },
    'studen3' : {
        'Name3' : "Rajulur" ,
        'age' : 26
    },
    'studen4' : {
        'Name4' : "RRTamim" ,
        'age' : 27
    },
    'studen5' : {
        'Name5' : "RRT" ,
        'age' : 28
    }
   
}
# for i in students[]:     
#     print(i)
# for i in students.values():
#     print (i)

# students["studen5"]["Name"]
# print (students)


dict_1={
    "key" : "RRT",
    'age':24
}
dict_1['key']
print(dict_1)



# for i in students.values():
# for i,j in students.items():
#     print(i,j)

for i in students.keys():
    print(i)
    




#2 Print all keys and values using loops.

students = {
    'studen1' : {
        'Name' : "Tamim" ,
        'age' : 24
    },
    'studen2' : {
        'Name' : "Rashid" ,
        'age' : 25
    },
    'studen3' : {
        'Name' : "Rajulur" ,
        'age' : 26
    },
    'studen4' : {
        'Name' : "RRTamim" ,
        'age' : 27
    },
    'studen5' : {
        'Name' : "RRT" ,
        'age' : 28
    }
   
}
# students["studen1"]['Name']='Shuvo'
# print(students)

for i, j in students.items():
    print(i, j)

# for i in students.keys():
#     print(i)
# for i in students.values():
#     print(f" value is {i['Name']}")


#3.Change the value of any key.

students = {
    "name" : "Shuvo" ,
    "age" : 24
}
students["name"] = 'Tamim'
print(students)

students = {
    'studen1' : {
        'Name' : "Tamim" ,
        'age' : 24
    }
}

students["studen1"]['Name']='Shuvo'
print(students)


#4 Use update() to add multiple new fields.

students = {
        'Name' : "Tamim" ,
        'age' : 24
    }
students.update(Roll=34)
print(students)
# students.update(students2)
# students.update(students3)
# print(students)
# Initial dictionary
# dict1 = {'X': 10}

# Add new key-value pairs
# dict1.update(Y=20, Z=30)
# print(dict1)
students.pop('Roll')

print(students)



#5  Create a nested dictionary and access nested values.

students = {
    'studen1' : {
        'Name' : "Tamim" ,
        'age' : 24
    },
    'studen2' : {
        'Name' : "Rashid" ,
        'age' : 25
    },
    'studen3' : {
        'Name' : "Rajulur" ,
        'age' : 26
    },
    'studen4' : {
        'Name' : "RRTamim" ,
        'age' : 27
    },
    'studen5' : {
        'Name' : "RRT" ,
        'age' : 28
    }

   
}

print(students['studen1']['Name'])


# 7 Count character frequency using a dictionary.
'''
text = "WeLoveTouch&solve"
count = 0
for i in text:
    count +=1
    print(i)
print(count)
'''

#8 Convert two lists into a dictionary:
# -- Keys → Names
# -- Values → Marks

Names = ["tamim","shuvo","morshed"]
Marks = [34,65,35]
dict_1 = dict(zip(Names,Marks))
print(dict_1)


#9 



student = {

    "name": "Rodri",
    "age": 22,
    "city": "Dhaka"
}
student['name']='Tamim'
print(student)


student1={
        'Name' : "Tamim" ,
        'age' : 24
    }


student1.update(roll=24)
student1.update(clsas=2)
print(student1)

# students.updates(student1.update(Name='tamim'))
# students['studen1'].update({"Name":"Rashid" , "age":27})
# print(students)

#Convert two lists into a dictionary:


# -- Keys → Names
# -- Values → Marks

name = ["Tamim", "Shuvo", "Hassan", "Nipu"]
marks = [97, 90, 85, 40]
var = dict (zip (name, marks))
print(var)

#Write a program that stores employee details and retrieves them by user input ID.


students = {
    'studen1' : {
        'Name' : "Tamim" ,
        'age' : 24
    },
    'studen2' : {
        'Name' : "Rashid" ,
        'age' : 25
    },
    'studen3' : {
        'Name' : "Rajulur" ,
        'age' : 26
    },
    'studen4' : {
        'Name' : "RRTamim" ,
        'age' : 27
    },
    'studen5' : {
        'Name' : "RRT" ,
        'age' : 28
    }

   
}
students['studen5'].update({
    "Roll":34
})
students.update({
    "studen6": {
    "Name":"Shuvo",
    "age" : 27}
})
print(students)


# while True:
#     name = input ("Enter a student name: ")
#     if name == quit:
#         print("Good bye everyone")
#         break
#     if name in students:
#         info = students[name]
#         print("Enmployee details")
#         print(info)
#     else:
#         print("Not found")

