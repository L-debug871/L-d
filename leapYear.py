# Name: Lerato Moholo
# Date: 02/08/2024
# Purpose: Determine whether a year is a leap year or not.
# A year is a leap year if (a) it is divisible by 400 
# or (b) it is divisible by 4 but not by 100

year = int(input("Enter a year:" "\n"))
rem1= year%400
rem2= year%4
rem3= year%100
if rem1==0 or rem2==0 and rem3!=0: #divisible by 400 or it is divisible by 4 but not by 100
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
