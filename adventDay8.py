outputs = []
tempPuts = []
counter = 0
f = open("myInputDay8.txt", "r")
for line in f:
    print(line)
    line = line.split(" | ")
    line = list(map(lambda x: str(x), line))
    tempPuts.append(line[1])
tempPuts = list(map(lambda jtem: jtem.replace("\n", ""), tempPuts))
print(tempPuts)
for item in tempPuts:
    for i in range(4):
        outputs.append(item.split(" ")[i])
print(outputs)
for jtem in outputs:
    print(len(jtem))
    if len(jtem) == 1 or len(jtem) == 4 or len(jtem) == 7 or len(jtem) == 8:
        counter += 1
print(counter)
