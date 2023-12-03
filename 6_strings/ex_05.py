str = 'X-DSPAM-Confidence: 0.8475 '
####instructions from PY4E####
#extract number
#convert to float

##we know that number is always after the colon 

# *find position of colon 
start = str.find(':')

# *strip whitespace from colon to end
number = float(str[start+1:].strip())

#*convert to float (done inline with strip^)

print(number)
