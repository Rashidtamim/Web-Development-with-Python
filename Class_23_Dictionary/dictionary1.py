# 1. Create a nested dictionary of 5 students (name and age)
students = {
    'student1': {
        'Name': 'Rajulur',    # Fixed the extra space bug (was 'Name ')
        'age': 24
    },
    'student2': {
        'Name': 'Rashid',
        'age': 25
    },
    'student3': {
        'Name': 'Tamim',
        'age': 26
    },
    'student4': {
        'Name': 'Rashid Tamim',
        'age': 27
    },
    'student5': {
        'Name': 'RRTamim',
        'age': 28
    }
}

# Print the entire dictionary to see the structure
print("Full students dictionary:")
print(students)



#  # 2. Print all students using loop (through .values())
print("Printing each student using loop:")
for student_data in students.values():   # .values() gives only inner dictionaries
    print(f"Name: {student_data['Name']}, Age: {student_data['age']}")



# 3. Change the value of any key (example with student1)
students['student1']['Name'] = 'Tamim Iqbal'   # Directly modify nested value
print(" After changing student1 name:")
print(students['student1'])



# 4. Use update() to add multiple new fields to a student
students['student3'].update({
    'grade': 'A+',
    'city': 'Dhaka',
    'hobby': 'Cricket',
    'joined_year': 2023
})
print("After adding new fields to student3 using update():")
print(students['student3'])



# 5. Remove items using pop() and del
removed_student4 = students.pop('student4')   # pop removes and returns the value
print("Removed student4 (using pop):")
print(removed_student4)

del students['student5']                      # del just removes, no return value
print("After deleting student5 (using del), remaining students:")
print(students.keys())



# 6. Access nested values (clean way with loop)
print("Accessing all nested values cleanly:")
for student_id, info in students.items():     # .items() gives key + inner dict
    print(f"{student_id} → Name: {info['Name']}, Age: {info['age']}")

    
employe = {
    "Tamim" : {
        "Subject": "English",
        "Marks": 65
    },
    "Shuvo" : {
       "Subject" : "Math",
       "Marks" : 78

    }
}
print(employe)



# 7. Count character frequency in a string using dictionary
text = "programming"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1           # increment if already exists
    else:
        char_count[char] = 1            # first time seeing this char


print(char_count)



# 8. Convert two lists into a dictionary using zip()
names = ['Tamim', 'Rashid', 'Shuvo', 'Morshed']
marks = [85, 92, 78, 88]

marks_dict = dict(zip(names, marks))   # zip pairs them → dict converts to dictionary
print("Names → Marks dictionary:")
print(marks_dict)



# 9. Interactive Employee Lookup System using nested dictionary
employees = {
    'E101': {'name': 'Rashid Tamim',   'dept': 'IT',        'salary': 75000, 'city': 'Dhaka'},
    'E102': {'name': 'Rajulur Rashid', 'dept': 'HR',        'salary': 68000, 'city': 'Chittagong'},
    'E103': {'name': 'Shuvo Hossen',   'dept': 'Finance',   'salary': 82000, 'city': 'Dhaka'},
    'E104': {'name': 'Hashem Ali',     'dept': 'Marketing', 'salary': 71000, 'city': 'Sylhet'}
}

print("9. Employee Lookup System (type 'quit' to exit)")
print("Available IDs:", list(employees.keys()))

while True:
    emp_id = input("\nEnter Employee ID (or 'quit' to exit): ").strip()

    if emp_id.lower() == 'quit':
        print("Goodbye!")
        break

    if emp_id in employees:
        info = employees[emp_id]
        print("\n--- Employee Details ---")
        print(f"Name    : {info['name']}")
        print(f"Department : {info['dept']}")
        print(f"Salary  : {info['salary']}")
        print(f"City    : {info['city']}")
    else:
        print("Employee ID not found! Try E101, E102, etc.")

