# Example 1:

# Input: 

nums1a = [2,3,2]
nums2a = [1,2]

# Output: [2,1]

# Explanation:



# Example 2:

# Input: 
nums1b = [4,3,2,3,1]
nums2b = [2,2,5,2,3,6]

# Output: [3,4]

# Explanation:

# The elements at indices 1, 2, and 3 in nums1 exist in nums2 as well. So answer1 is 3.

# The elements at indices 0, 1, 3, and 4 in nums2 exist in nums1. So answer2 is 4.

# Example 3:

# Input: 
nums1c = [3,4,2,3]
nums2c = [1,5]

# Output: [0,0]

# Explanation:

# No numbers are common between nums1 and nums2, so answer is [0,0].

def findIntersectionValues(nums1, nums2):
    return [
        sum(1 for num in nums1 if num in nums2),
        sum(1 for num in nums2 if num in nums1)
    ]

print(findIntersectionValues(nums1a, nums2a))
print(findIntersectionValues(nums1b, nums2b))
print(findIntersectionValues(nums1c, nums2c))