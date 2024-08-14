# Example 1:

# Input: 
nums1 = [1,1,1]
# Output: 3
# Explanation: You can do the following operations:
# 1) Increment nums[2], so nums becomes [1,1,2].
# 2) Increment nums[1], so nums becomes [1,2,2].
# 3) Increment nums[2], so nums becomes [1,2,3].
# Example 2:

# Input: 
nums2 = [1,5,2,4,1]
# Output: 14
# Example 3:

# Input: 
nums3 = [8]
# Output: 0

def minOperations(nums) -> int:
    count = 0
    start = nums[0]
    for i in range(1, len(nums)):
        increase = 0
        if nums[i] <= start:
            increase = (start + 1) - nums[i]
            count += increase
        start = nums[i] + increase
    return count

print(minOperations(nums1))
print(minOperations(nums2))
print(minOperations(nums3))

def minOperations1(nums) -> int:
    count = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            increase = (nums[i-1] + 1) - nums[i]
            count += increase
            nums[i] += increase
    return count

print(minOperations1(nums1))
print(minOperations1(nums2))
print(minOperations1(nums3))