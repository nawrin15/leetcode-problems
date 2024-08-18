# Example 1:

# Input: 
nums1 = [1,5,0,3,5]
# Output: 3
# Explanation:
# In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
# In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
# In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
# Example 2:

# Input: 
nums2 = [0]
# Output: 0
# Explanation: Each element in nums is already 0 so no operations are needed.

def minimumOperations(nums) -> int:
    return len(set(nums)) - (0 in nums)



print(minimumOperations(nums1))
print(minimumOperations(nums2))
