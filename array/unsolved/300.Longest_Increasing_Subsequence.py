# Example 1:

# Input: 
nums1 = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Example 2:

# Input: 
nums2 = [0,1,0,3,2,3]
# Output: 4
# Example 3:

# Input: 
nums3 = [7,7,7,7,7,7,7]
# Output: 1

def lengthOfLIS(nums):
    n = len(nums)
    maxi = [1] * n
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                maxi[i] = max(maxi[i], maxi[j] + 1)
    return max(maxi)

print(lengthOfLIS(nums1))
print(lengthOfLIS(nums2))
print(lengthOfLIS(nums3))