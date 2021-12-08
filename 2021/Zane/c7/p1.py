#!/usr/bin/python3
with open("input.txt", "r") as f:
	crabs = sorted([int(crab) for crab in f.read().split(",")])
if len(crabs) % 2 == 1:
	median = crabs[(len(crabs)-1)/2]
else:
	median = int((crabs[int(len(crabs)/2)-1] + crabs[int(len(crabs)/2)])/2)

fuelcost = 0
for crab in crabs:
	fuelcost += abs(crab-median)
print(fuelcost)
