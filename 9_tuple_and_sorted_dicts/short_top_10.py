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

#shorter version using list comprehension
tmp = ( sorted ( [ (v,k) for k,v in words.items() ] ) ) 


for val, key in tmp[:10]:
        print(key, val)
                        