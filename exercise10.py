text = input("Enter a sentence: ")

count = 0

for char in text:
    if char.lower() in "aeiou":
        count += 1

print("Total vowels:", count)
#output:
Enter a sentence: Hello World
Total vowels: 3
