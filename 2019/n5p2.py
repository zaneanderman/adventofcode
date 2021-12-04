#!/usr/bin/python3
codes = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,34,7,225,101,17,169,224,1001,224,-92,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,46,28,225,1102,66,83,225,2,174,143,224,1001,224,-3280,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,19,83,224,101,-102,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1001,114,17,224,1001,224,-63,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,60,46,225,1101,7,44,225,1002,40,64,224,1001,224,-1792,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,80,27,225,1,118,44,224,101,-127,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,75,82,225,1101,40,41,225,1102,22,61,224,1001,224,-1342,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,102,73,14,224,1001,224,-511,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,344,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,359,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,374,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,389,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,404,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,677,677,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,449,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,464,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,479,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,494,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,7,677,226,224,1002,223,2,223,1006,224,524,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,539,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,569,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,7,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,629,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,644,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,659,101,1,223,223,107,226,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]
#stupid intcode...

inputvariable = 5
pointer = 0
pointerincrement = 0
default = "0"

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
		print("directnumber%i"%codes[pointer+1])
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

