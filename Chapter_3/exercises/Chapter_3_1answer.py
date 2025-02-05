## PROMPT ##
""""
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly.
"""


# takes in hours and converts to float
hrs = input("Enter Hours:")
h = float(hrs)

# takes in hourly rate and converts to float
rate = input("Enter Hourly Rate:")
r = float(rate)

total_pay = 0

# if overtime:
if h > 40:
    # calculate overtime pay and add it to total_pay
    overtime = h - 40
    overtime_pay = overtime * ( 1.5 * r)
    total_pay = total_pay + overtime_pay
    
    # set hours to 40 for calculating regular pay
    h = 40.0

#calculate regular pay
total_pay = total_pay + ( h * r )

#output result
print(total_pay)







## NOTES ##
# Desired input: 45
# Desired input: 10.50
# Desired output: 498.75