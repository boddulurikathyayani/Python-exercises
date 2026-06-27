num = int(input("Enter a number: "))

print("Digits in reverse order:")

while num > 0:
    digit = num % 10
    print(digit)
    num = num // 10
  #output:
  Enter a number: 7536
Digits in reverse order:
6
3
5
7
