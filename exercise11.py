numbers = [10, 5, 20, 2, 45, 7]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)
#output:
Largest number: 45
Smallest number: 2
