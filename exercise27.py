dict1 = {
    "name": "Kathyayani",
    "age": 18
}

dict2 = {
    "course": "CSE",
    "college": "Vignan"
}

# Merge dictionaries
merged_dict = {**dict1, **dict2}

print("Merged Dictionary:")
print(merged_dict)
#output:
Merged Dictionary:
{'name': 'Kathyayani', 'age': 18, 'course': 'CSE', 'college': 'Vignan'}
