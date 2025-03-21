# chr= ["a","b","b","c","c","c","c","c","c","c","c","c","c"]
# from collections import defaultdict

# def sl(char):
	
# 	pre = chr[0] 
# 	for i in range(len(char)):
# 		c = char[]
# 	# print(d)
# 	# s=""
# 	# for a in d:
# 	# 	if d[a] == 1:
# 	# 		s += str(a) 
# 	# 	else:
# 	# 		s += a
# 	# 		s += str(d[a])
# 	return s
	
# print(sl(chr))
nums = [1,2,3,1, 4, 3]

nums = [1,2,1,3,5,6,6]

def findPeak(num):
	res  = []
	prev = num[0]
	if len(nums) == 1:
		return nums
	for i in range(1, len(num)):
		n = num[i]
		if n < prev:
			res.append(prev)
		prev = num[i]
	return res

print(findPeak(nums))
		