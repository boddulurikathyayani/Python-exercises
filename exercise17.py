num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
  #output:
  Enter a number: 121
Palindrome Number
Enter a number: 123
Not a Palindrome Number
