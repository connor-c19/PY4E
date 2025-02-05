## PROMPT ##
""""
3.3 Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. 
For the test, enter a score of 0.85.
"""

score = input("Enter Score: ")

# check if score is float
is_float = True

try: 
    score = float(score)
except:
    is_float = False

# if no error is thrown
if is_float == True:
    
    # if score isn't less than 0 or greater than 1
    if 0.0 <= score <= 1.0:
        
        # find out the letter grade
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")

# Otherwise, print error message        
else:
    print("Invalid score. Make sure it is a float between 0.0 and 1.0")
        


## NOTES ##
# Desired input: 0.85
# Desired output: "B"