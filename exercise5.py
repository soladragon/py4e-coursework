fi = open("mbox-short.txt")
mylist = []
mycount = 0
for text in fi:
    if text.startswith('From'):
        x = text.split()
        mycount += 1
        print(x[1])
print("There were " + str(mycount) + " lines in the file with From as the first word")

