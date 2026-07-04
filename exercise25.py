n = 15

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
  #output:
  Fibonacci Series:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
