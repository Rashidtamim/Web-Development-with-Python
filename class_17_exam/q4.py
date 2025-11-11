#remove all duplicate values from a list while mainting the original order.

# Take input
n = int(input("Enter the size of the list: "))
lst = []

print("Enter the numbers:")
for i in range(n):
    lst.append(int(input()))

print("Original List =",lst)

unique = list(set(lst))
print("This is after remove the duplicate file",unique)

# new_list = []
# [new_list.append(x) for x in lst if x not in new_list]
# print(new_list)

'''# Take input
n = int(input("Enter size of list: "))
lst = []

print("Enter the numbers:")
for i in range(n):
    lst.append(int(input()))

# Remove duplicates but keep original order
new_list = []
seen = []  # to track which numbers we already added

for num in lst:
    if num not in seen:      # if we haven't seen this number before
        new_list.append(num) # add it to new list
        seen.append(num)     # now mark it as "seen"

# Print result
print("Original list    :", lst)
print("Without duplicates:", new_list)'''
