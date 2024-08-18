# Example 1:

# Input: 
nums1 = [1,2,5,2,3]
target1 = 2
# Output: [1,2]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The indices where nums[i] == 2 are 1 and 2.
# Example 2:

# Input: 
nums2 = [1,2,5,2,3]
target2 = 3
# Output: [3]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 3 is 3.
# Example 3:

# Input: 
nums3 = [1,2,5,2,3]
target3 = 5
# Output: [4]
# Explanation: After sorting, nums is [1,2,2,3,5].
# The index where nums[i] == 5 is 4.

def targetIndices(nums, target: int):
    res = []
    nums.sort()
    n = len(nums)
    for i in range(len(nums)):
        if target == nums[i]:
            res.append(i)
            if n > i + 1 and nums[i+1] != target:
                break
    return res

print(targetIndices(nums1, target1))
print(targetIndices(nums2, target2))
print(targetIndices(nums3, target3))

def targetIndices1(nums, target: int):
    res = []
    nums.sort()
    n = len(nums)
    for i in range(len(nums)):
        if target == nums[i]:
            res.append(i)
        elif nums[i] > target:
                break
    return res

print(targetIndices1(nums1, target1))
print(targetIndices1(nums2, target2))
print(targetIndices1(nums3, target3))

