#!/usr/bin/python3
import random
codes = [3,8,1001,8,10,8,105,1,0,0,21,46,59,80,105,122,203,284,365,446,99999,3,9,102,3,9,9,1001,9,5,9,102,2,9,9,1001,9,3,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,102,4,9,9,101,3,9,9,102,2,9,9,4,9,99,3,9,102,5,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99]
backupsoftware = codes.copy()
inputvariable = 5
pointer = 0
pointerincrement = 0
default = "0"
outputvalue = 0
dictofphasesettings = {}

def multipladditionoutputting(mode, parameter1mode, parameter2mode): #multipladditionoutputting, your catch-all function for multiplication, addition and outputting
	global codes, pointerincrement, pointer
	parameter1 = codes[pointer+1]
	parameter2 = codes[pointer+2]
	#print("parameter1mode")
	#print(parameter1mode)
	#print("parameter2mode")
	#print(parameter2mode)
	if parameter1mode == "0":
		parameter1 = safe_list_get(codes, parameter1)
	if parameter2mode == "0":
		parameter2 = safe_list_get(codes, parameter2)

	multipliednumber = int(parameter1)*int(parameter2)
	addednumber = int(parameter1)+int(parameter2)
	if mode == "2":
		codes[codes[pointer+3]] = multipliednumber
		pointerincrement = 4
	elif mode == "1":
		codes[codes[pointer+3]] = addednumber
		pointerincrement = 4
	
	elif mode == "4":
		print("output: %i"%parameter1)
		outputvalue = parameter1
		pointerincrement = 2
	elif mode == "5":
		if parameter1 != 0: 
			pointer = parameter2
			pointerincrement = 0
		else:
			pointerincrement = 3
	elif mode == "6":
		if parameter1 == 0:
			pointer = parameter2
			pointerincrement = 0
		else:
			pointerincrement = 3
	elif mode == "7":
		if parameter1 < parameter2:
			codes[codes[pointer+3]] = 1
		else:
			codes[codes[pointer+3]] = 0
		pointerincrement = 4
	elif mode == "8":
		if parameter1 == parameter2:
			codes[codes[pointer+3]] = 1
		else:
			codes[codes[pointer+3]] = 0
		pointerincrement = 4
	else:
		print("fatal code %s"%mode)
		exit()


def safe_list_get(l, idx):
	try:
		return l[idx]
	except IndexError:
		return default

for i in range(0, 120):
	phasesettings = random.sample(range(5), 5)
	while str(phasesettings) in dictofphasesettings:
		phasesettings = random.sample(range(5), 5)
	dictofphasesettings[str(phasesettings)] = True
	for i in range(0, 5):
		while True:
			code = str(codes[pointer])
			print("pointer")
			print(pointer)
			print("code")
			print(code)

			if code == "99": #end at a 99
				break
			
			if code == "3":
				codes[codes[pointer+1]] = inputvariable #thing at second argument becomes input variable
				pointerincrement = 2
			
			if int(code[-1]) in range(1, 9) and int(code[-1]) != 3:
				multipladditionoutputting(code[-1], safe_list_get(code, -3), safe_list_get(code, -4))
			pointer += pointerincrement
		if i == 4:

		codes = backupsoftware.copy()

