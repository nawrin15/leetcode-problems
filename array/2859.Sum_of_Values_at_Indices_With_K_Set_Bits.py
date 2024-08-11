# Example 1:

# Input: 
nums1 = [5,10,1,5,2]
k1 = 1
# Output: 13
# Explanation: The binary representation of the indices are: 
# 0 = 000
# 1 = 001
# 2 = 010
# 3 = 011
# 4 = 100 
# Indices 1, 2, and 4 have k = 1 set bits in their binary representation.
# Hence, the answer is nums[1] + nums[2] + nums[4] = 13.
# Example 2:

# Input: 
nums2 = [4,3,2,1]
k2 = 2
# Output: 1
# Explanation: The binary representation of the indices are:
# 0 = 00
# 1 = 01
# 2 = 10
# 3 = 11
# Only index 3 has k = 2 set bits in its binary representation.
# Hence, the answer is nums[3] = 1.

def sumIndicesWithKSetBits(nums, k: int) -> int:
    res = 0
    for i in range(len(nums)):
        if bin(i)[2:].count('1') == k:
            res += nums[i]
    return res

print(sumIndicesWithKSetBits(nums1, k1))
print(sumIndicesWithKSetBits(nums2, k2))

def sumIndicesWithKSetBits2(nums, k: int) -> int:
    return sum([nums[i]if bin(i).count('1') == k else 0 for i in range(len(nums))])
       

print(sumIndicesWithKSetBits2(nums1, k1))
print(sumIndicesWithKSetBits2(nums2, k2))