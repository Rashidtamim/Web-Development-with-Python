#Find all pairs of numbers in a list whose sum equals a given target
# Take input
n = int(input("Enter size of list: "))
lst = []

print("Enter the elements:")
for i in range(n):
    lst.append(int(input()))

# How many positions to rotate right
k = int(input("Enter rotation positions (k): "))

# Make k smaller (in case k > n)
k = k % n   # Super important line!

# METHOD: Slice and join
rotated = lst[-k:] + lst[:-k]

# Print result
print("Original list :", lst)
print(f"After rotating {k} positions to RIGHT:")
print("Rotated list  :", rotated)