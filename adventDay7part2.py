f = open("myInputDay7.txt", "r")
positions = f.readline().split(",")
positions = list(map(lambda x: int(x), positions))
print(positions)
listOfFuels = []
for i in range(max(positions)):
    fuel = 0
    for item in positions:
        n = abs(item - i)
        fuel = n * (n + 1) / 2 + fuel
    listOfFuels.append(fuel)
print(min(listOfFuels))
