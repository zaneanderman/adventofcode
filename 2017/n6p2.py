#!/usr/bin/python3
from collections import defaultdict

def wrapperfunction(runningsecondtime, array):
	
	positions = defaultdict(lambda: 0)
	counter = 0

	while True:
		positions[str(array)] = 1

		biggestnumber = -1
		for i in range(0, len(array)):
			if array[i] > biggestnumber:
				biggestnumber = array[i]
				location = i
		blocks = array[location]
		array[location] = 0
		for i in range(1, blocks+1):
			array[(location+i)%len(array)] += 1

		counter += 1

		if str(array) in positions:
			if runningsecondtime:
				print(counter)
				exit()
			else:
				return array
wrapperfunction(True, wrapperfunction(False, [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]))