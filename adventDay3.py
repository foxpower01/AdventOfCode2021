f = open("myInputDay3.txt", "r")
num1 = []
num0 = []
gamma = []
epsilon = []

for i in range (12):
    f.seek(0)
    for line in f:
        if list(line)[i] == "0":
            if len(num0) <= i:
                num0.append(1)
            else:
                num0[i] += 1
        if list(line)[i] == "1":
            if len(num1) <= i:
                num1.append(1)
            else:
                num1[i] += 1

for i in range (12):
    if num1[i] < num0[i]:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

gammaBin = "".join(map(str, gamma))
epsilonBin = "".join(map(str, epsilon))
print(int(gammaBin, 2) * int(epsilonBin, 2))