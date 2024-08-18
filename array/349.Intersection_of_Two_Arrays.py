# Example 1:

# Input: 
nums1a = [1,2,2,1]
nums2a = [2,2]
# Output: [2]
# Example 2:

# Input: 
nums1b = [4,9,5]
nums2b = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return list(nums1 & nums2)
    return nums2.intersection(nums1)

from collections import Counter

def intersection1(nums1, nums2):
    d = Counter(nums1)
    res = set()
    for num in nums2:
        if num in d:
            res.add(num)
    return res

print(intersection(nums1a, nums2a))
print(intersection(nums1b, nums2b))
print(intersection1(nums1a, nums2a))
print(intersection1(nums1b, nums2b))

