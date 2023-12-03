def biggest_smallest (num):
    print("Enter 'L' to find the largest number in the list.\n Enter 'S' to find the smallest number in the list\n")
    while True:
        arg = input()
        if arg == 'L':
            max = num[0]
            for number in num:
                if number > max:
                    max = number
            return(max)
        if arg == 'S':
            min = num[0]
            for number in num:
                if number < min:
                    min = number
            return(min)
        else: print("Enter either 'L' or 'S' ")


num = []
print("\n***Largest/smallest value calculator***\nPlease enter a number. Submit 'q' when all numbers have been entered:\n")
while True:
    val = input()
    if val == 'q':
        break
    if val.isdigit():
        num.append((val))
    else:
        print("Please enter a valid number or 'q'\n")

print("Your number is: ", biggest_smallest(num))

