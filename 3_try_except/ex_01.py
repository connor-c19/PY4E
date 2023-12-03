try: 
    hours = float((input("Enter Hours: ")))
    rate = float((input("Enter Rate: ")))

except:
    print("Error, please enter numerical input")
    quit()


# if else block checks to see if overtime is entered
if (hours) > 40:
    overtime = (hours - 40) * (rate * 1.5)
    pay = 40 * rate + overtime

else: pay = (hours) * (rate)

print("Pay: ",round(pay, 2)) 