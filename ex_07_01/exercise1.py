fi = open("mbox-short.txt")

for text in fi:
    stripped = text.rstrip()
    uppercaps = stripped.upper()
    print(uppercaps)