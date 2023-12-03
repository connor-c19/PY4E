#ask user for file name 
name = input('Enter file:')
#open file, reads line by line
handle = open(name)

counts = dict()

for line in handle:
    #creates list of words
    words = line.split()
    #creates dictionary of words
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#flip 
tmp = []
for k, v in counts.items():
			tmp.append( (v, k) )
#sort by descending order                 
tmp = sorted(tmp, reverse = True)

for val, key in tmp[:10]:
        print(key, val)
                        

