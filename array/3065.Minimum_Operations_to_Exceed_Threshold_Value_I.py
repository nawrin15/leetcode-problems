# Example 1:

# Input: 
nums1 = [2,11,10,1,3]
k1 = 10
# Output: 3
# Explanation: After one operation, nums becomes equal to [2, 11, 10, 3].
# After two operations, nums becomes equal to [11, 10, 3].
# After three operations, nums becomes equal to [11, 10].
# At this stage, all the elements of nums are greater than or equal to 10 so we can stop.
# It can be shown that 3 is the minimum number of operations needed so that all elements of the array are greater than or equal to 10.
# Example 2:

# Input: 
nums2 = [1,1,2,4,9]
k2 = 1
# Output: 0
# Explanation: All elements of the array are greater than or equal to 1 so we do not need to apply any operations on nums.
# Example 3:

# Input: 
nums3 = [1,1,2,4,9]
k3 = 9
# Output: 4
# Explanation: only a single element of nums is greater than or equal to 9 so we need to apply the operations 4 times on nums.

def minOperations(nums, k: int) -> int:
    return sum(1 for num in nums if num < k)

print(minOperations(nums1, k1))
print(minOperations(nums2, k2))
print(minOperations(nums3, k3))

def minOperations1(nums, k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= k:
                return i
        return -1

print(minOperations1(nums1, k1))
print(minOperations1(nums2, k2))
print(minOperations1(nums3, k3))