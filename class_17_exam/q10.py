#Remove elements from a list that appear more than once and keep only unique ones.

# Take input
n = int(input("Enter size of list: "))
lst = []

print("Enter the elements:")
for i in range(n):
    lst.append(int(input()))

# Remove elements that appear more than once
unique_once = []

for i in range(n):
    count = 0
    for j in range(n):
        if lst[i] == lst[j]:
            count += 1
    
    # If this number appears exactly ONCE
    if count == 1:
        # Add only if not already added (avoid duplicates in result)
        if lst[i] not in unique_once:
            unique_once.append(lst[i])

# Print result
print("Original list         :", lst)
print("Elements appear once  :", unique_once)