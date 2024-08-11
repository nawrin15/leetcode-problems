# Example 1:

# Input: 
nums1a = [1,3,4]
nums2a = [1,3,4]
ka = 1

# Output: 5

# Explanation:

# The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
# Example 2:

# Input: 
nums1b = [1,2,4,12]
nums2b = [2,4]
kb = 3

# Output: 2

# Explanation:

# The 2 good pairs are (3, 0) and (3, 1).

def numberOfPairs(nums1, nums2, k: int) -> int:
    count = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % (nums2[j] * k) == 0:
                count += 1
    return count

print(numberOfPairs(nums1a, nums2a,ka))
print(numberOfPairs(nums1b, nums2b,kb))