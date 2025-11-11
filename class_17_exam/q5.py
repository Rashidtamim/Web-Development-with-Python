#Count how many elements are greater than the average of the list.

# Take input
n = int(input("Enter the size of the list: "))
lst = []
lst2 = []

print("Enter the numbers:")
for i in range(n):
    lst.append(int(input()))

print("Original List =",lst)
average = sum(lst)/len(lst)
print(average)

for i in lst:
    if average < i :
        lst2.append(i)
    else:
        None
print(lst2)
print(len(lst2))

































'''
# Take input
n = int(input("Enter the size of the list: "))
lst = []

print("Enter the numbers:")
for i in range(n):
    lst.append(int(input()))

# Step 1: Calculate sum of all numbers
total = 0
for num in lst:
    total += num

# Step 2: Calculate average
average = total / n

# Step 3: Count how many are greater than average
count = 0
for num in lst:
    if num > average:
        count += 1

# Print everything nicely
print("Original list   :", lst)
print("Sum             :", total)
print("Average         :", average)
print("Numbers > average:", count)

'''