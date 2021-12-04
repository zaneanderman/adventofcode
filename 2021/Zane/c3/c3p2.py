import copy
with open("input.txt", "r") as f:
	generator = f.read().split("\n")[:-1]
print(generator)
#generator = ["111111010011","110011001100","010011111000","101001100011","011011100110","110100011011","001000001010","011011101000","110011001000","001011101010","100000001000","001000000111","111110110101","101000100110","110101110001","101101010111","000010001001","101110010100","101000101011","010110100011","110010011001","110110011111","100111000001","100101010011","101011011001","111101110010","000111000001","000000000111","011010111101","101010100011","010001001011","100011010100","100000011110","000010110100","101001110100","000110110000","101100101000","111001100111","110100001110","001111000110","101111101110","011101111100","000010001111","010100101001","111101000001","110010111111","111011001111","001101011101","101001111001","111100000010","111101101111","001011000100","100010001011","111111001110","010010111011","000110010001","001011100001","011010101011","101011000010","100111010000","100110010101","010000100010","101101100011","100110000001","001011011010","101100111110","011101101111","110000011010","101111000100","100011000011","001110000101","011110110010","111110010001","010000111110","001101100001","001010101111","010011011000","101000101101","000110111100","000000100001","110000101000","000000001001","100001111111","100111111011","010011110010","110100101110","100101110001","000111011000","101101111000","000110001001","110001101110","111011001110","011001111010","011100000110","111000000111","100100011100","001001111100","011101001101","000111110000","001000110100","111001000110","110010001101","011011010101","011110011011","010110001100","111000001010","101101000001","101000011111","010110011011","000001101010","001100001001","000111111100","011000101001","011000101110","001001100011","111111111101","011010100010","010011010101","110010101100","100111101010","101110000111","100101010000","001001110010","100001100110","111001011000","100111010111","100111111110","110101010110","110000001110","001000110111","111101000110","110111101010","000100001101","011000011110","010110000000","111001111100","111111000001","111101001111","100001011011","000000110011","000010011111","100110001111","010001011011","111010100011","011001111100","110100001100","010000000101","101011001000","000011001111","111101111100","101111001011","011110011110","110101111001","010111000100","101100100100","010111100111","101111011010","110110110101","000110111010","010111010011","110000111010","011101001010","111011101111","010010000010","101111110001","110001101101","111101001010","010010110111","101110110011","101001100101","100000000001","000100000001","011001101110","010010111110","010000011111","101010101010","101001010111","010000001000","110001001011","100001110111","011111110010","100000100001","101101100101","100011110101","000100111110","001101010001","100010111101","010111100000","100001010001","000100111111","011100011000","010001100111","011000011011","011100000001","100101100110","110101010100","000000001101","001111100000","011111000010","101011010101","110011011000","000000111111","001100101001","010100110111","100000010010","101100010000","111111111010","100110000000","011111001100","011101001001","010011100101","010110010011","010011000000","111100011011","001001010010","010011001111","010100000101","111100110101","011011110011","011000110100","101111110000","011001000001","000111100000","110011111001","111010000001","001100011010","101010010110","100010111000","111111010000","010100111110","000001010100","001011101011","010000111010","110010100100","001101110100","001010001000","110110101010","110100101111","010010101100","011011111101","010011001100","011010011111","100110010100","010010011100","100010010101","010100111011","101101010100","001111111001","101101111110","000100101000","000100001110","101111001000","100101110011","111011111010","011010100101","100011000101","111100100110","011101111101","100111101001","010101110111","110100100111","001111100010","010111100011","101111011111","101111111101","101000001011","000011010111","000101001000","101111101111","100011101010","011111100110","000101010110","000000001010","000010110001","011101010101","011111010010","010001110000","101101000101","110100010110","100010100101","110010111101","010101111110","010111011010","111110011001","110010000110","100100111000","100011100101","001101011010","111000110000","111110010100","111000111000","101101000010","000111101110","110101011101","010100010001","011100001101","011101000000","100001011010","101001010010","110111011101","100000010110","010100110010","010000111011","101111111000","111000111101","001011110010","101001000001","011100110101","101101011111","111001101111","001110100010","001000011000","100000000011","011011100111","000101010001","100001110010","000111101000","111101101101","011101011001","110100010111","011101100010","101100110010","001101010011","010110010110","101001010100","011011000001","110001111001","111010011101","101001111000","110011011111","100110110110","001111011011","111100111110","010100000001","101111010101","011110100110","101100111101","010101100011","000011000011","011001001000","110000001100","101100000111","000000011110","100110000010","111001111010","000111001100","111011111100","100111001111","110010100001","100010001111","000010000110","111000101000","101011110001","101011011110","110111111110","010100101111","011100110000","011001101001","110101111100","001101110011","110110001101","011110111100","010011101000","011101101011","001010001111","000001001011","001101110001","000011001011","110100110110","110000111011","100001111110","010101010000","011000000101","110101001111","111001010000","000110110011","110001001110","110100111110","001010010101","001111011101","101000010001","101110100000","010110111111","111001001011","010011000101","010101010011","010010100110","000101000101","111011100001","100110110111","110111011000","111011110010","000100011110","110000111100","000000101100","101011010100","010100100100","011111101111","101001100100","001000011010","011000001100","111110100100","100101110111","011110110100","001011011000","111101011101","010111011101","100000100010","011100111111","111010100110","001011101110","000110111000","001011110000","101000110111","001101001111","000100001000","100000110110","000101100001","111010111101","010111001000","011110001101","001010011101","001010111100","010110111101","111110001111","011011010000","111011111001","111011010011","010111010010","000101110111","011000010000","010000100111","001111110000","011001101010","001110001111","101010000101","011011001100","110101000000","011000111011","010110001110","101101001001","111100001101","101011000000","110010000100","011000111110","100111100011","101010100001","100011101110","000100110010","100011111001","101100100110","101101011101","100111000110","111111100100","101001111111","010011111111","010111000000","101110001111","011000110000","100110110100","101010000110","101011000110","110001110100","110100111101","100110101101","001001101101","000001011001","010011001110","011010010010","011011011011","010100000010","100111001010","110101011111","001000101111","110100100001","101010111001","010111011100","010111011000","111000101110","111101000111","111000110001","000000111110","011101110001","011100100011","100110001100","001101000101","111000110101","011000101000","010110110100","101111101010","101001011111","101000111111","101001110110","100001010100","111111101101","110010111011","100111000111","000001111100","011010101000","100101101111","000110011111","101010011010","010000101101","001111001111","100100110111","001101000000","000110101010","011110001011","110001100111","000001101101","111001001111","000100010111","100001000110","000010110010","000100001010","001010100111","101000010110","011011011001","010011010001","100100011000","001111110110","110111100111","101110110100","101100001111","011001010001","001110110010","001000111011","110011000000","001101010111","110101100000","100011111010","110101000010","001100010001","001100110100","000100000111","001010111101","101001101000","010010000111","000100000010","001100000100","101000100010","010010100101","000110111111","001100100001","110001101010","001010110001","110111110000","100011100001","101000010000","101001000100","101101011110","010000110100","110100110010","110000010001","111110101010","110010101011","110101110110","111101101000","101010100111","101101101111","101010110101","001101010100","001101101100","010111001011","100000011011","111101001101","001110010111","010000110111","010000110110","111100110111","011100111010","010100011101","000011011101","111111110001","110000111000","110000110000","010011110011","011101000101","011011001011","111000011100","011111111100","100011001111","000101111110","001001110111","100111011011","011110110111","100100010011","010100110101","010001101000","011000001111","110011110001","110011000101","110011100100","011001001111","010100000110","011110010010","110101010101","000011011001","101011110011","101110011001","001111000100","110110111011","010101001011","011100100100","110010000010","000010000111","000101100100","001100100110","011011101010","111000010101","010000000100","111001110110","110000110111","111001001100","100011111011","010001001111","101100110000","010011011100","000001000101","011010011010","000010111001","110000101101","111010011000","110111011100","011100001110","011010001111","111110010011","111011010100","101101001011","010100001011","100011101100","010011101101","000101010000","110011011001","100100010111","111111010110","101011111011","010001110101","010001010010","100111100010","100000110000","011011000110","000110000100","100011110110","010111000011","100010100111","010010000001","111011001011","000100010110","101101011011","100101010001","111001111110","000111100010","010111011111","000110010100","110100000100","001000100101","001000100001","111100001010","001101010010","100101100011","101011001100","001110000010","011011010110","001001011111","111011100100","110100111000","000101100101","001001110100","000011000110","001110101101","110100111011","101011101110","110001001001","001000001100","101111111100","110011000010","001111001011","101100101110","110010111110","011101110000","101110010111","001011000111","011110010011","110111001100","111011110111","110111110011","010111100110","110011000111","101011011010","011100000101","101001111101","010001000001","011100100001","010110101010","001111101100","010000000110","010010010111","000110110101","101110110101","111010000000","101100011010","010010100000","001001000110","000010101110","100100110000","110101100001","100010011111","010110111110","000101100111","111010000010","110011010011","110011101001","101000100011","010101000101","111100111001","010011101010","001111101110","011000110010","001001000001","100011111111","101110100011","001011101001","010001011000","011111101100","110101010000","110110101100","111101110000","000001011010","100111001011","011101000110","010001000000","111001000100","000010100001","011000101010","010011010111","010100100011","001110011011","001101110000","101100000010","101111000000","100001111101","000000011101","111011010010","001110101111","010100001110","110001110010","001000011110","111100000011","111010100101","000101011010","100111110111","010100000100","011101001011","000010011100","001000010010","110100000001","011101100100","000100110001","001000000000","101111110011","000111010101","011110100011","110000001101","000001001100","111101110111","001100001111","101010001101","010011000111","100000000100","100100011001","100011100011","111110100011","111101100110","000000101001","101010100100","000100010000","010110001000","010110010000","100011000100","111011011001","100111111001","000011101111","101011001011","111110100010","000000010101","100111000000","000110010101","100101011111","010110011110","110110110011","100111011100","010000100101","011010101010","110111000111","110110000000","110111101101","001001101001","100101101000","001011100111","100010110100","011001111000","111110000000","010011101011","100010111010","101011101001","010110000110","001100010111","100010000110","100011001000","101111011110","110101101110","001110101001","010111111110","010011110111","100101001101","010111001101","001000110010","011110001110","111001110011","111001001101","000101110101","011011100010","001100011011","000011110001","111101111011","111101100010","111010001001","101001101101","100101011000","010011000010","110011000100","111100001001","010001110111","001011110110","110010011011","101000000111","100001110000","110111110010","000111011110","101010101101","110001000101","100100001101","111101100100","010000001001","011101001100","111010100001","101010010010","110111010111","000111011100","101101111010","110000010111","100100100000","101111011000","111011101100","110101101010","110111101011","001110100001","100110110011","011011011101","011001011000","101100011001","100000011100","111100010101","011100010111","010001111011","000000101110","000011011100","011100010000","011000001011","111110101110","111011010110","110110000011","011011010010","011111101101","001011001101","000101011100","111010001101","100001010111","010010100100","001011111000","000011010101","010100001001","101100101100","000000100010","001100110000","001010010111","101100110101","000001011000","001100110110","101000111100","111011111111","011010010000","100100111010","010000101001","110000110010","011010001011","001000001000","111010100000","101010101011","101000110100","100110000011","001100011110","001010100100","111111101001","101100001001","111111011110","000110001100","100101000100","000111101001","011000000110","101110001000","000110001000","001000100100","100100010110","010101110011","011101111000","111110010010","110110100010","010001001110","101011101100","101011011100","110001111011","110100010001","001100110001","001010111001","110011111000","110010101010","001010001100","101010001100","010100010100","111101100000","100100000101","100011011110","000111111011","010001101010","111001101011","001011001010","000101100000","010101011001","011110010101","010000110000","100101101001","110111110001","000100011111","010001101101","111010110101","011010011000","110011100000","101111100000","001011011101","010110000010","101000001110","101010000111","101000101110","101111001101","110110001111","100001011110","010111110100","110011000001","000111000100","010011100111","101011011101","111100001110","101000110010","100111111000","110101101001","001010010001","101110011110","100001001010","100111001100","110111101110","100011000001","111111010101","011111111101","100110111101","000111001110","000111011011","000001001010","000011010100","001100001011","100111010110","101011000111","011111100111","000001000100","100000101110","110110100111","111100000000","001100001101","011111100101","101110001100","000111000110","101010111011","101111001010","100110010011","000110101111","001010000010","100010000100","110001000110","101100100111"] 
scrubber = copy.copy(generator)
for arraytype in ["generator", "scrubber"]:
	nums = {"generator":generator, "scrubber":scrubber}[arraytype]
	for pointer in range(12):
		if len(nums) == 1:
			break
		ones = []
		zeros = []
		for num in nums:
			{"1":ones, "0":zeros}[num[pointer]].append(num)
		print(len(ones))
		print(len(zeros))
		if (arraytype == "generator" and len(ones) >= len(zeros)) or (arraytype == "scrubber" and len(ones) < len(zeros)):
			nums = copy.copy(ones)
			print(arraytype, "ones")
		else:
			nums = copy.copy(zeros)
			print(arraytype, "zeros")
		print(pointer)
		print(nums)
	if arraytype == "generator":
		generator = copy.copy(nums)
		print("gen")
	else:
		scrubber = copy.copy(nums)
		print("scrub")
print(generator, scrubber)
print(int(generator[0], 2)*int(scrubber[0], 2))