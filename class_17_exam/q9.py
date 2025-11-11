#Find the most frequent element in a list (without using counter or external libraries)
# Take input
n = int(input("Enter size of list: "))
lst = []

print("Enter the elements:")
for i in range(n):
    lst.append(int(input()))

# Find most frequent element
max_count = 0
most_freq = lst[0]  # assume first is most frequent

for i in range(n):
    count = 0
    for j in range(n):
        if lst[i] == lst[j]:
            count += 1
    
    if count > max_count:
        max_count = count
        most_freq = lst[i]

# Print result
print("Original list   :", lst)
print("Most frequent   :", most_freq)
print("Appears         :", max_count, "times")