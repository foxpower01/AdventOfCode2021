from os import read

f = open("myInputFile.txt", "r")
myInput = []
listOfSums = []
counter = 0

def isBiggerThanLast(index, list):
    if list[index] > list[index - 1]:
        return(True)
    else:
        return(False)

for line in f:
    myInput.append(line)

for i in range (0, len(myInput)):
    if i + 2 < len(myInput):
        listOfSums.append(int(myInput[i]) + int(myInput[i + 1]) + int(myInput[i + 2]))

for i in range (0, len(listOfSums)):
    if isBiggerThanLast(i, listOfSums):
        counter += 1

print(counter)