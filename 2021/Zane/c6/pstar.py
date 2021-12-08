#!/usr/bin/python3
import copy
import functools
fish = [0]*9
with open("input.txt") as f:
	for i in f.read().split(","):
		fish[int(i)] += 1
for i in range(256):
	newfish = [0]*9
	for j in range(1, len(fish)):
		newfish[j-1] = fish[j]
	newfish[6] += fish[0]
	newfish[8] += fish[0]	
	fish = copy.copy(newfish)
	if i == 79:
		print(functools.reduce(lambda a, b: a+b, fish))

print(functools.reduce(lambda a, b: a+b, fish))
