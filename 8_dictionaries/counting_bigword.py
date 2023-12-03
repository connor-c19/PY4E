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


bigcount = None
bigword = None
#iterates through tuple of each key+value combo
for word,count in counts.items():
    #initializes bigcount first, then checks to see which word has the biggest count 
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print("The most used word is '" + bigword + "' with " + str(bigcount) + " mentions")