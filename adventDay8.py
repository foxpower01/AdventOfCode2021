outputs = []
f = open("myInputDay8.txt", "r")
for line in f:
    line = line.split(" | ")
    line = list(map(lambda x: str(x), line))
    outputs.append(line[1])
outputs = list(map(lambda jtem: jtem.replace("\n", ""), outputs))