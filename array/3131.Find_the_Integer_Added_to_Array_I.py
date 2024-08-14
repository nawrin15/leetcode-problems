# # Example 1:

# Input: 
nums1a = [2,6,4]
nums2a = [9,7,5]

# Output: 3

# Explanation:

# The integer added to each element of nums1 is 3.

# Example 2:

# Input: 
nums1b = [10]
nums2b = [5]

# Output: -5

# Explanation:

# The integer added to each element of nums1 is -5.

# Example 3:

# Input: 
nums1c = [1,1,1,1]
nums2c = [1,1,1,1]

# Output: 0

# Explanation:

# The integer added to each element of nums1 is 0.

def addedInteger(nums1, nums2) -> int:
    return int((sum(nums2) - sum(nums1))/len(nums2))
    s1 = sum(nums1)
    s2 = sum(nums2)
    diff = s2 - s1
    n = len(nums2)
    return int(diff/n)

print(addedInteger(nums1a, nums2a))
print(addedInteger(nums1b, nums2b))
print(addedInteger(nums1c, nums2c))

def addedInteger1(nums1, nums2) -> int:
    return min(nums2) - min(nums1)

print(addedInteger1(nums1a, nums2a))
print(addedInteger1(nums1b, nums2b))
print(addedInteger1(nums1c, nums2c))