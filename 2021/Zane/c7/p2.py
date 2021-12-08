with open("input.txt", "r") as f:
	crabs = sorted([int(crab) for crab in f.read().split(",")])
pos = 0
while True:
 	backcrabs = [crab for crab in crabs if crab <= pos]
 	frontcrabs = crabs[len(backcrabs):]
 	cost = 0
 	save = 0
 	for crab in backcrabs:
 		cost += (pos-crab)+1
 	for crab in frontcrabs:
 		save += (crab-pos)
 	if cost > save:
 		break
 	pos += 1

fuelcost = 0
for crab in crabs:
	fuelcost += abs(pos-crab)*(abs(pos-crab)+1)/2
print(int(fuelcost))

