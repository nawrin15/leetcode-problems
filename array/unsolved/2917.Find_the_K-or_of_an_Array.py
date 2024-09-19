# Example 1:

# Input: 
nums1 = [7,12,9,8,9,15]
k1 = 4

# Output: 9

# Explanation:

# Represent numbers in binary:

# Number	Bit 3	Bit 2	Bit 1	Bit 0
# 7	0	1	1	1
# 12	1	1	0	0
# 9	1	0	0	1
# 8	1	0	0	0
# 9	1	0	0	1
# 15	1	1	1	1
# Result = 9	1	0	0	1
# Bit 0 is set in 7, 9, 9, and 15. Bit 3 is set in 12, 9, 8, 9, and 15.
# Only bits 0 and 3 qualify. The result is (1001)2 = 9.

# Example 2:

# Input: 
nums2 = [2,12,1,11,4,5]
k2 = 6

# Output: 0

# Explanation: No bit appears as 1 in all six array numbers, as required for K-or with k = 6. Thus, the result is 0.

# Example 3:

# Input: 
nums3 = [10,8,5,9,11,6,8]
k3 = 1

# Output: 15

# Explanation: Since k == 1, the 1-or of the array is equal to the bitwise OR of all 
# its elements. Hence, the answer is 10 OR 8 OR 5 OR 9 OR 11 OR 6 OR 8 = 15.

def findKOr(nums, k: int) -> int:
    
    return 