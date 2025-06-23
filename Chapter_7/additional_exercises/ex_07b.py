##search through file 
#Look for lines that begin with "from"
#extract third word (using split())
hand = open('file.txt')
##search through each line of the file
for line in hand:
	line = line.rstrip()
	words = line.split()
	#guardian pattern, protects next line of code from blowing up
	if len(words) < 3 or words[0] != 'From':
		continue 
	print(words[2])
		


