#!/usr/bin/python3
#never decrease, two adjacent
from collections import defaultdict
numcounter = 0
for i in range(145852, 616942):
	num = str(i)
	previousdigit = -10
	adjacent = "no"
	decrease = "no"
	Dict = defaultdict(lambda: 0)
	for digit in num:
		Dict[digit] += 1
		if int(digit) < previousdigit:
			decrease = "yes"
			break
		previousdigit = int(digit)
	for i in Dict.values():
		if i == 2:
			adjacent = "yes"
	if adjacent == "yes" and decrease == "no":
		numcounter += 1
print(numcounter)


