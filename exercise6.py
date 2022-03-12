l = []
answer = ""


while answer != "done":
    print("Please enter a range of numbers")
    answer = input()
    # print(answer)
    if answer != "done":
        l.append(answer)
print("Maximum: " + str(max(l)))
print("Minimum: " + str(min(l)))