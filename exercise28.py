list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

# Find common elements
common = set(list1) & set(list2)

print("Common elements:", common)
#output:
Common elements: {40, 50, 30}
