# Example 1:

# Input: 
nums1 = [5,3,6,1,12]
original1 = 3
# Output: 24
# Explanation: 
# - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
# - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
# - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
# - 24 is not found in nums. Thus, 24 is returned.
# Example 2:

# Input: 
nums2 = [2,7,9] 
original2 = 4
# Output: 4
# Explanation:
# - 4 is not found in nums. Thus, 4 is returned.

def findFinalValue(nums, original: int) -> int:
    nums = set(nums)
    flag = 1
    while flag:
        if original in nums:
            original *= 2
            continue 
        flag = 0
    return original

print(findFinalValue(nums1, original1))
print(findFinalValue(nums2, original2))

def findFinalValue(nums, original: int) -> int:
    nums = set(nums)
    while original in nums:
        original *= 2
    return original

print(findFinalValue(nums1, original1))
print(findFinalValue(nums2, original2))