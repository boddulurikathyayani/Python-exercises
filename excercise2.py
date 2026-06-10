def calculate(num1, num2):
    product = num1 * num2
    
    if product <= 1000:
        return product
    else:
        return num1 + num2

# Test cases
result1 = calculate(20, 30)
print("The result is", result1)

result2 = calculate(40, 30)
print("The result is", result2)

# Output:
# The result is 600
# The result is 70
