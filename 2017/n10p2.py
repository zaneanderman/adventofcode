chars = "83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100"
lengths = list(ord(i) for i in chars)+[17, 31, 73, 47, 23]

skip = 0 
nums = list(range(256))
pointer = 0
for i in range(64):
	for length in lengths:
		if length + pointer < 256:
			chunk = nums[pointer:pointer+length][::-1]
			nums = nums[:pointer]+chunk+nums[pointer+length:]
		else:
			chunk = (nums[pointer:]+nums[:(pointer+length)%256])[::-1]
			nums = chunk[len(chunk)-((pointer+length)%256):] + nums[(pointer+length)%256:pointer] + chunk[:len(chunk)-((pointer+length)%256)]
		pointer = (pointer+length+skip)%256
		skip += 1
dense = []
for i in range(16):
	num = nums[i*16]
	for j in range(1, 16):
		num ^= nums[i*16+j]
	dense.append(num)

for i in range(len(dense)):
	dense[i] = ("0"+(hex(dense[i])[2:]))[-2:]
print("".join(dense))


