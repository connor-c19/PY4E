#initialization of dictionary
counts = dict()

#prompt for input
line = input("Enter a line of text:\n")

#split string into list
words = line.split()

#count each word by creating a dictionary key for each new word
for word in words:
    counts[word] = counts.get(word, 0) + 1

#print result
print(counts)

