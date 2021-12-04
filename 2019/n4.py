#!/usr/bin/python3
#never decrease, two adjacent
numcounter = 0
for i in range(145852, 616942):
	num = str(i)
	previousdigit = -10
	adjacent = "no"
	decrease = "no"
	for digit in num:
		if int(digit) < previousdigit:
			decrease = "yes"
			break
		if int(digit) == previousdigit:
			adjacent = "yes"
		previousdigit = int(digit)
	if adjacent == "yes" and decrease == "no":
		numcounter += 1
print(numcounter)


