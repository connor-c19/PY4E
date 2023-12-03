total = 0
count = 0
while True:
    number = input("Enter a number: ")
    if number == 'done': break
    try: 
        total += float(number)
        count += 1
    except:
        print("Invalid input\n")
#prints total, count, and avg of inputs 
print(total, count, total/count)
