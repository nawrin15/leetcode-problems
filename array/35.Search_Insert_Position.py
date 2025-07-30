# Example 1:

nums1 = [1,3,5,6]
target1 = 5
# Output: 2
# Example 2:

# Input: 
nums2 = [1,3,5,6] 
target2 = 2
# Output: 1
# Example 3:

# Input: 
nums3 = [1,3,5,6]
target3 = 7
# Output: 4

def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return i + 1

print(searchInsert(nums1, target1))
print(searchInsert(nums2, target2))
print(searchInsert(nums3, target3))

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(searchInsert(nums1, target1))
print(searchInsert(nums2, target2))
print(searchInsert(nums3, target3))