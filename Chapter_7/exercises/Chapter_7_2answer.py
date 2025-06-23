## PROMPT ##
"""
7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
"""

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")

fh = open(fname)


values = 0
count = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
        
    #extract the floating point values from each of the lines 
    ## get value in string form 
    value_start_index = line.find(":")
    value_string = line[value_start_index+1:]
    value_string_stripped = value_string.strip()
    
    ## convert string value to float
    value_float = float(value_string_stripped)
    
    
    #compute the average of those values and produce an output as shown below.
    values += value_float
    count += 1
        
print("Average spam confidence: "+ str(values/count))










## NOTES ##
# Desired input: mbox-short.txt
# Desired output: Average spam confidence: 0.7507185185185187