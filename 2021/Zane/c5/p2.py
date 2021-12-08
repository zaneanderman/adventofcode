#!/usr/bin/python3
from collections import defaultdict
with open("input.txt", "r") as f:
	lines = f.readlines()
ventcount = defaultdict(lambda: 0)
for line in lines:
	split = line[:-1].split(" -> ")
	nums = split[0].split(",")+split[1].split(",")
	print(nums)
	if nums[0] == nums[2]:
		direction = {True:-1, False:1}[int(nums[1]) >= int(nums[3])]
		for i in range(int(nums[1]), int(nums[3])+direction, direction):
			ventcount[nums[0]+","+str(i)] += 1
	
	elif nums[1] == nums[3]:
		direction = {True:-1, False:1}[int(nums[0]) >= int(nums[2])]
		for i in range(int(nums[0]), int(nums[2])+direction, direction):
			ventcount[str(i)+","+nums[1]] += 1

	elif abs(int(nums[0])-int(nums[2])) == abs(int(nums[0])-int(nums[2])): #if the x and y differences are the same, i.e. a 45 degree line
		directionx = {True:-1, False:1}[int(nums[0]) >= int(nums[2])]
		directiony = {True:-1, False:1}[int(nums[1]) >= int(nums[3])]
		j = int(nums[1])
		for i in range(int(nums[0]), int(nums[2])+directionx, directionx):
			ventcount[str(i)+","+str(j)] += 1
			j += directiony

def show(ventcount):
	for i in range(10):
		for j in range(10):
			print(ventcount[str(j)+str(i)], end="")
		print("")
show(ventcount)
counter = 0
print(ventcount.keys())
for i in ventcount.values():
	if i > 1:
		counter+=1
print(counter)

