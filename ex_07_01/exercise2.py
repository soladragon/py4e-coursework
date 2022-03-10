print("Please enter the filename you want to scan:")
answer = input()

fi = open(answer + ".txt")
count = 0
total_confidence = 0
for text in fi:
    if text.startswith("X-DSPAM-Confidence:"):
        spaceindex = text.find(" ")
        confi = float(text[spaceindex + 1 :])
        count += 1
        total_confidence += confi

print("The average total confidence is: ", total_confidence/count)