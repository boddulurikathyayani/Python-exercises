paragraph = "python is easy python is powerful and python is fun"

words = paragraph.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Count:")
print(word_count)
#output:
Word Count:
{'python': 3, 'is': 3, 'easy': 1, 'powerful': 1, 'and': 1, 'fun': 1}
