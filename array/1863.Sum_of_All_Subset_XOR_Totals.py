# Example 1:

# Input: 
nums1 = [1,3]
# Output: 6
# Explanation: The 4 subsets of [1,3] are:
# - The empty subset has an XOR total of 0.
# - [1] has an XOR total of 1.
# - [3] has an XOR total of 3.
# - [1,3] has an XOR total of 1 XOR 3 = 2.
# 0 + 1 + 3 + 2 = 6
# Example 2:

# Input: 
nums2 = [5,1,6]
# Output: 28
# Explanation: The 8 subsets of [5,1,6] are:
# - The empty subset has an XOR total of 0.
# - [5] has an XOR total of 5.
# - [1] has an XOR total of 1.
# - [6] has an XOR total of 6.
# - [5,1] has an XOR total of 5 XOR 1 = 4.
# - [5,6] has an XOR total of 5 XOR 6 = 3.
# - [1,6] has an XOR total of 1 XOR 6 = 7.
# - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
# 0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

def subsetXORSum(nums) -> int:
    
    return