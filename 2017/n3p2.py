#!/usr/bin/python3
from collections import defaultdict
import time
directions = ["down", "right", "up", "left"]
direction = "right"
number = 1
amount = 1
position = [0, 0]
grid = defaultdict(lambda: 0)
def turn():
	global direction
	direction = directions[(directions.index(direction)+1)%4] #next direction, circular
def move():
	global number, grid, position
	grid[str(position[0])+":"+str(position[1])] = number
	for i in range(0, amount):
		grid[str(position[0])+":"+str(position[1])] = number
		if direction == "down":
			position[1] -= 1
		elif direction == "up":
			position[1] += 1
		elif direction == "left":
			position[0] -= 1
		elif direction == "right":
			position[0] += 1
		increment()
		check()
def increment():
	global number
	number = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			if not (i == 0 and j == 0):
				
				number += grid[str(position[0]+i)+":"+str(position[1]+j)]

def check():
	if number >= 289326:
		print(number)
		exit()
while True:
	move()
	turn()
	move()
	turn()
	amount += 1

