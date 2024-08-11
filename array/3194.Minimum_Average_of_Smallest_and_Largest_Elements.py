# Example 1:

# Input: 
nums1 = [7,8,3,4,15,13,4,1]

# Output: 5.5

# Explanation:

# step	nums	averages
# 0	[7,8,3,4,15,13,4,1]	[]
# 1	[7,8,3,4,13,4]	[8]
# 2	[7,8,4,4]	[8,8]
# 3	[7,4]	[8,8,6]
# 4	[]	[8,8,6,5.5]
# The smallest element of averages, 5.5, is returned.
# Example 2:

# Input: 
nums2 = [1,9,8,3,10,5]

# Output: 5.5

# Explanation:

# step	nums	averages
# 0	[1,9,8,3,10,5]	[]
# 1	[9,8,3,5]	[5.5]
# 2	[8,5]	[5.5,6]
# 3	[]	[5.5,6,6.5]
# Example 3:

# Input: 
nums3 = [1,2,3,7,8,9]

# Output: 5.0

# Explanation:

# step	nums	averages
# 0	[1,2,3,7,8,9]	[]
# 1	[2,3,7,8]	[5]
# 2	[3,7]	[5,5]
# 3	[]	[5,5,5]

def minimumAverage(nums) -> float:
    nums = sorted(nums)
    res = []
    n = len(nums)
    for i in range(n//2):
        res.append((nums[i] + nums[n-1-i])/2)
    return min(res)

print(minimumAverage(nums1))
print(minimumAverage(nums2))
print(minimumAverage(nums3))