#!/usr/bin/python3
from collections import defaultdict
pointer = 0
tape = defaultdict(lambda: 0)
iterations = 0
#begin in state a.
#Perform a diagnostic checksum after 12964419 steps.
answer = 0
nextstate = "A"
while iterations < 12964419:
	iterations += 1
	"""
	if nextstate == "a":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer += 1
			nextstate = "b"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 1
			pointer += 1
			nextstate = "f"

	elif nextstate == "b":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 0
			pointer -= 1
			nextstate = "b"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 1
			pointer -= 1
			nextstate = "c"

	elif nextstate == "c":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer -= 1
			nextstate = "d"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 0
			pointer += 1
			nextstate = "c"

	elif nextstate == "d":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer -= 1
			nextstate = "e"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 1
			pointer += 1
			nextstate = "a"

	elif nextstate == "e":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer -= 1
			nextstate = "f"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 0
			pointer -= 1
			nextstate = "d"

	elif nextstate == "f":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer += 1
			nextstate = "a"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 0
			pointer -= 1
			nextstate = "e"
			"""
	if nextstate == "A":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer += 1
			nextstate = "B"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 0
			pointer += 1
			nextstate = "F"

	elif nextstate == "B":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 0
			pointer -= 1
			nextstate = "B"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 1
			pointer -= 1
			nextstate = "C"

	elif nextstate == "C":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer -= 1
			nextstate = "D"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 0
			pointer += 1
			nextstate = "C"

	elif nextstate == "D":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer -= 1
			nextstate = "E"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 1
			pointer += 1
			nextstate = "A"

	elif nextstate == "E":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer -= 1
			nextstate = "F"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 0
			pointer -= 1
			nextstate = "D"

	elif nextstate == "F":
		if tape[str(pointer)] == 0:
			tape[str(pointer)] = 1
			pointer += 1
			nextstate = "A"
		elif tape[str(pointer)] == 1:
			tape[str(pointer)] = 0
			pointer -= 1
			nextstate = "E"
	else:
		print("fatal nextstate %s, [insert explosion noise here]"%nextstate)

for i in tape.values():
		if i == 1:
			answer += 1
print(answer)