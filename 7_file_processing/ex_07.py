#prints the contents of a file in uppercase ... not too useful 
while True:
    name = input("Enter a file name: ")
    try:
        fhand = open(name)
    except:
        print("Invalid file name:", name)
        continue
    for x in fhand:
        x = x.rstrip()
        print(x.upper())
    break

