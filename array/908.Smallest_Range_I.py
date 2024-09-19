# Example 1:

# Input: 
nums1 = [1]
k1 = 0
# Output: 0
# Explanation: The score is max(nums) - min(nums) = 1 - 1 = 0.
# Example 2:

# Input: 
nums2 = [0,10]
k2 = 2
# Output: 6
# Explanation: Change nums to be [2, 8]. The score is max(nums) - min(nums) = 8 - 2 = 6.
# Example 3:

# Input: 
nums3 = [1,3,6]
k3 = 3
# Output: 0
# Explanation: Change nums to be [4, 4, 4]. The score is max(nums) - min(nums) = 4 - 4 = 0.
 
def smallestRangeI(nums, k: int) -> int:
    mini = min(nums)
    maxi = max(nums)
    if mini + k >= maxi -k:
        return 0
    else:
        return (maxi - k) - (mini + k)
    
print(smallestRangeI(nums1, k1))
print(smallestRangeI(nums2, k2))
print(smallestRangeI(nums3, k3))

def smallestRangeI(nums, k: int) -> int:
    mini = min(nums)
    maxi = max(nums)
    return max(0, maxi - k - (mini + k) )
    
print(smallestRangeI(nums1, k1))
print(smallestRangeI(nums2, k2))
print(smallestRangeI(nums3, k3))


