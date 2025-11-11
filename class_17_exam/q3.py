#Find the Second largest number in a list without using max() or sort() function
# Take input
n = int(input("Enter the size of the list: "))
lst = []

print("Enter the numbers:")
for i in range(n):
    lst.append(int(input()))

# Initialize with first two elements (safe way)
first = lst[0]
second = lst[0]

# First, find the largest
for i in range(n):
    if lst[i] > first:
        first = lst[i]
print("Largest Number is",first)

# Then, find second largest (must be smaller than first)
for i in range(n):
    if lst[i] > second and lst[i] < first:
        second = lst[i]

# Check if second largest exists
if second == first or n < 2:
    print("No second largest number exists!")
else:
    print("Second largest number is:", second)