def exponent(base, exp):
    result = 1

    for i in range(exp):
        result = result * base

    return result

# Input
base = int(input("Enter base: "))
exp = int(input("Enter exponent: "))

# Function call
print("Result:", exponent(base, exp))
#output:1
Enter base: 2
Enter exponent: 5
Result: 32
#output:2
Enter base: 3
Enter exponent: 4
Result: 81
