d = {'a': 10, 'c': 11, 'b': 12, }

#sort dictionary
# #d.items creates a list of tuples representing the dictionary  
sorted_dic = sorted(d.items())

#for loop iterates through both elements of tuple 
for k, v in sorted_dic:
    print(k, v)