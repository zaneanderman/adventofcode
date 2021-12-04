lengths = [83,0,193,1,254,237,187,40,88,27,2,255,149,29,42,100]
skip = 0 
nums = list(range(256))
pointer = 0
for length in lengths:
	if length + pointer < 256:
		chunk = nums[pointer:pointer+length][::-1]
		nums = nums[:pointer]+chunk+nums[pointer+length:]
	else:
		chunk = (nums[pointer:]+nums[:(pointer+length)%256])[::-1]
		nums = chunk[len(chunk)-((pointer+length)%256):] + nums[(pointer+length)%256:pointer] + chunk[:len(chunk)-((pointer+length)%256)]
	pointer = (pointer+length+skip)%256
	skip += 1
	print(nums)

print(nums[0]*nums[1])
