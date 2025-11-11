#Flatten a nested list(a list within a list) into a single list.
# Take input (example nested list)
nested_list = []
n = int(input("Enter number of main elements: "))

print("Enter elements (use [] for sub-lists):")
for i in range(n):
    item = input(f"Element {i+1}: ")
    # Convert string input to actual list using eval
    nested_list.append(eval(item))

# Flatten the list
flat_list = []

for item in nested_list:
    if type(item) == list:          # If it's a sub-list
        for sub_item in item:       # Add each element one by one
            flat_list.append(sub_item)
    else:                           # If it's a single number/string
        flat_list.append(item)

# Print result
print("\nOriginal nested list :", nested_list)
print("Flattened list       :", flat_list)