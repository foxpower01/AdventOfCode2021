outputs = []
tempPuts = []
posA = posB = posC = posD = posE = posF = posG = 0
counter = 0
tempJtem = []
f = open("myInputDay8.txt", "r")

def isOne(item):
    if len(item) == 2:
        return(True)

def isSeven(item):
    if len(item) == 3:
        return(True)

def isFour(item):
    if len(item) == 4:
        return(True)

def isEight(item):
    if len(item) == 7:
        return(True)

for line in f:
    print(line)
    line = line.split(" | ")
    line = list(map(lambda x: str(x), line))
    print(line)
    tempPuts.append(line[1])
temPuts = list(map(lambda jtem: jtem.replace("\n", ""), tempPuts))
for line in tempPuts:
    outputs.append(line.split(" "))
print(outputs)
#for item in tempPuts:
#    for i in range(4):
#        outputs.append(item.split(" ")[i])
#print(outputs)
#for jtem in outputs:
#    print(len(jtem))
#    if len(jtem) == 2 or len(jtem) == 3 or len(jtem) == 4 or len(jtem) == 7:
#        counter += 1
#print(counter)
for line in outputs:
    print(line)
    for item in line:
        print(item)
        if len(item) == 2:
            tempItem = list(item)
            print(tempItem)
            print("hi")

