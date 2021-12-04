#!/usr/bin/python3
directions = ["down", "right", "up", "left"]
direction = "down"
number = 1
amount = 1
position = [0, 0]
def turn():
	global direction
	direction = directions[(directions.index(direction)+1)%4] #next direction, circular
def move():
	global number
	for i in range(0, amount):
		number += 1
		if direction == "down":
			position[1] -= 1
		if direction == "up":
			position[1] += 1
		if direction == "left":
			position[0] -= 1
		if direction == "right":
			position[0] += 1
		check()
def check():
	if number == 289326:
		print(abs(position[1])+abs(position[0]))
		exit()
while True:
	move()
	turn()
	move()
	turn()
	amount += 1

