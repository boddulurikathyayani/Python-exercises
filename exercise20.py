income = float(input("Enter your income: "))

tax = 0

if income <= 10000:
    tax = 0
elif income <= 20000:
    tax = (income - 10000) * 0.10
else:
    tax = 10000 * 0.10 + (income - 20000) * 0.20

print("Income Tax =", tax)
#output1:
Enter your income: 8000
Income Tax = 0
#output2:
Enter your income: 15000
Income Tax = 500.0
