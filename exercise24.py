num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a Palindrome")
else:
    print(original, "is not a Palindrome")
  #output:1
  Enter a number: 121
  121 is a Palindrome 
#output:2 
Enter a number: 123
123 is not a Palindrome
