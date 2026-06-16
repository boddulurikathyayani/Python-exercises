fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print("Original list:", fruits)

# Add new fruit
fruits.append("mango")

# Remove second fruit (index 1)
fruits.pop(1)

print("Updated list:", fruits)
#output:
Original list: ['apple', 'banana', 'cherry', 'date', 'elderberry']
Updated list: ['apple', 'cherry', 'date', 'elderberry', 'mango']
