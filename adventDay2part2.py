from os import read


horizontal = 0
depth = 0
aim = 0
f = open("myInputDay2.txt", "r")

for line in f:
    if line.split( )[0] == "forward":
        horizontal += int(line.split( )[1])
        depth +=  aim * int(line.split( )[1])
    elif line.split( )[0] == "down":
        aim += int(line.split( )[1])
    else:
        aim -= int(line.split( )[1])

print(horizontal)
print(depth)
print(horizontal * depth)

print(line.split()[1])