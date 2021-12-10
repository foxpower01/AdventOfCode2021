f = open("myInputDay3.txt", "r")
num0 = 0
num1 = 0
i = 0
myInput = []
myInput2 = []
MostFrequent = []

def isKept(counter, frequent, item):
    if list(item)[counter] == frequent:
        return(True)
    else:
        return(False)

f.seek(0)
for line in f:
    myInput.append(line)
    myInput2.append(line)

while len(myInput) > 1:
    print(len(myInput))
    num1 = 0
    num0 = 0
    for item in myInput:
        if list(item)[i] == "0":
            num0 = num0 + 1
            print(num0)
        if list(item)[i] == "1":
            print(num1)
            num1 = num1 + 1
    print(num0, num1)
    print(num0 > num1, i)
    print(myInput)
    if num0 > num1:
        myInput = list(filter(lambda itemOfIn: isKept(i, "0", itemOfIn), myInput))
    else:
        myInput = list(filter(lambda itemOfIn2: isKept(i, "1", itemOfIn2), myInput))
    i += 1
print(myInput)

i = 0

while len(myInput2) > 1:
    print(len(myInput2))
    num1 = 0
    num0 = 0
    for item in myInput2:
        if list(item)[i] == "0":
            num0 += 1
        if list(item)[i] == "1":
            num1 += 1
    print(num0 > num1, i)
    print(myInput2)
    if num0 > num1:
        myInput2 = list(filter(lambda itemOfIn: isKept(i, "1", itemOfIn), myInput2))
        print(len(myInput2))
        print("hi")
    else:
        myInput2 = list(filter(lambda itemOfIn2: isKept(i, "0", itemOfIn2), myInput2))
        print(len(myInput2))
    i += 1
print(myInput2)
print(myInput)
print(int(myInput[0], 2) * int(myInput2[0], 2))