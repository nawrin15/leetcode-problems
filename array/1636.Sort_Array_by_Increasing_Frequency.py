# Example 1:

# Input: 
nums1 = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
# Example 2:

# Input: 
nums2 = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
# Example 3:

# Input: 
nums3 = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]

from collections import Counter

def frequencySort(nums):
    counter = Counter(nums)
    print(counter)
    return 

print(frequencySort(nums1))
print(frequencySort(nums2))
print(frequencySort(nums3))