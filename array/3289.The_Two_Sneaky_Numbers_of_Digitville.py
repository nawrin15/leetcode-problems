# Example 1:

# Input: 
nums1 = [0,1,1,0]

# Output: [0,1]

# Explanation:

# The numbers 0 and 1 each appear twice in the array.

# Example 2:

# Input: 
nums2 = [0,3,2,1,3,2]

# Output: [2,3]

# Explanation:

# The numbers 2 and 3 each appear twice in the array.

# Example 3:

# Input: 
nums3 = [7,1,5,4,3,4,6,0,9,5,8,2]

# Output: [4,5]

# Explanation:

# The numbers 4 and 5 each appear twice in the array.

from collections import Counter
from pandas import DataFrame

def getSneakyNumbers(nums):
    ctr = Counter(nums)
    return DataFrame.nlargest(2, ctr, key = lambda x: ctr[x])

print(getSneakyNumbers(nums1))
print(getSneakyNumbers(nums2))
print(getSneakyNumbers(nums3))