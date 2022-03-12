fi = open("romeo.txt")
mylist = []
for text in fi:
    x = text.split()
    for i in x:
        if i not in mylist:
            mylist.append(i)
            print("The word is not in the list!")

print(mylist)


