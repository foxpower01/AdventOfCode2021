f = open("myInputDay3.txt", "r")
num0 = 0
num1 = 0
i = 0
myInput = []
MostFrequent = []

def isKept(counter, frequent, item):
    if list(item)[counter] == frequent:
        return(True)
    else:
        return(False)

for line in f:
    myInput.append(line)

while len(list(myInput)) > 1:
    for item in myInput:
        num1 = 0
        num0 = 0
        if list(item)[i] == "0":
            num0 += 1
        if list(item)[i] == "1":
            num1 += 1
    if num0 > num1:
        myInput = filter(lambda item: isKept(i, 0, item), myInput)
        print(myInput)
    else:
        myInput = filter(lambda item: isKept(i, 1, item), myInput)
        print(myInput)
    i += 1
print(myInput)