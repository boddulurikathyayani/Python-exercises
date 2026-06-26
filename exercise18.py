list1 = [10, 21, 33, 40, 55]
list2 = [11, 22, 34, 45, 60]

new_list = []

# Add odd numbers from list1
for num in list1:
    if num % 2 != 0:
        new_list.append(num)

# Add even numbers from list2
for num in list2:
    if num % 2 == 0:
        new_list.append(num)

print("New List:", new_list)
#output:
New List: [21, 33, 55, 22, 34, 60]
