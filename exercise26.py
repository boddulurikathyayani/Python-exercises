year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
  #output:1
  Enter a year: 2024
2024 is a Leap Year
#output:2
Enter a year: 1900
1900 is not a Leap Year
