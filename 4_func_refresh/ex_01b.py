def computepay(hours, rate):
    pay = hours * rate 
    return pay

#try except block accounts for non-float/integer input
try: 
    hours = float((input("Enter Hours: ")))
    rate = float((input("Enter Rate: ")))

except:
    print("Error, please enter numerical input")
    quit()


# if else block checks to see if overtime is entered
if hours > 40:
    overtime = computepay(hours - 40, rate * 1.5)
    pay = computepay(40, rate) + overtime

else: pay = computepay(hours, rate)

print("Pay: ",round(pay, 2)) 