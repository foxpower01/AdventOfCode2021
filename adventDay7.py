f = open("myInputDay7.txt", "r")
positions = f.readline().split(",")
positions = list(map(lambda x: int(x), positions))
print(positions)
listOfFuels = []
for i in range(max(positions)):
    fuel = 0
    for item in positions:
        fuel = abs(item - i) + fuel
    listOfFuels.append(fuel)
print(min(listOfFuels))
