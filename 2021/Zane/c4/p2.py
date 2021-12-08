#!/usr/bin/python3
from copy import copy
with open("cards.txt", "r") as f:
	lines = [line for line in f.readlines() if line.strip()]
	cards = []
	completions = []
	pointer = 0
	while pointer < len(lines):
		if pointer % 5 == 0:
			cards.append([])
			completions.append([])
		cards[-1].append([i for i in lines[pointer].split() if i])
		completions[-1].append([False]*5)
		pointer += 1
with open("draws.txt", "r") as f:
	draws = f.read().split(",")


def findnum(card, number):
	for i in range(5):
		for j in range(5):
			if card[i][j] == number:
				return (i,j)
	return None
def is_complete(completion):
	counter = 0
	for i in range(5):
		counter = 0
		for j in range(5):
			if completion[i][j]:
				counter += 1
		if counter == 5:
			return True
	for i in range(5):
		counter = 0
		for j in range(5):
			if completion[j][i]:
				counter += 1
		if counter == 5:
			return True
	return False
def sumunmarked(card, completion):
	number = 0
	for i in range(5):
		for j in range(5):
			if not completion[i][j]:
				number += int(card[i][j])
	return number


completes = [False]*len(cards)
#emptycard = [[False]*5]*5
#completions = [copy(emptycard)]*len(cards)

for num in draws:
	for index, card in enumerate(cards):
		numpos = findnum(card, num)
		if numpos:
			completions[index][numpos[0]][numpos[1]] = True
			if is_complete(completions[index]):
				completes[index] = True
				if completes.count(False) == 0:
					print(sumunmarked(card, completions[index])*int(num))
					exit()
