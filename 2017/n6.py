#!/usr/bin/python3
array = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
from collections import defaultdict
positions = defaultdict(lambda: 0)
counter = 0

def log():
	positions[str(array)] = 1

def redistribute():
	biggestnumber = -1
	for i in range(0, len(array)):
		if array[i] > biggestnumber:
			biggestnumber = array[i]
			location = i

	blocks = array[location]
	array[location] = 0
	for i in range(1, blocks+1):
		array[(location+i)%len(array)] += 1

def check():
	if str(array) in positions:
		print(counter)
		exit()

while True:

	log()
	redistribute()
	counter += 1
	check()