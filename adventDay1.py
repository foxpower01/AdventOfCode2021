from os import read

f = open("myInputDay1.txt", "r")
myInput = []
counter = 0

def isBiggerThanLast(index, list):
    if list[index] > list[index - 1]:
        return(True)
    else:
        return(False)

for line in f:
    myInput.append(line)

print(myInput)

for i in range (0, len(myInput)):
    if i != 0 and isBiggerThanLast(i, myInput):
        counter += 1

print(counter)