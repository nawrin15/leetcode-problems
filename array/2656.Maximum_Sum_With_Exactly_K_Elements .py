# Example 1:

# Input: 
nums1 = [1,2,3,4,5]
k1 = 3
# Output: 18
# Explanation: We need to choose exactly 3 elements from nums to maximize the sum.
# For the first iteration, we choose 5. Then sum is 5 and nums = [1,2,3,4,6]
# For the second iteration, we choose 6. Then sum is 5 + 6 and nums = [1,2,3,4,7]
# For the third iteration, we choose 7. Then sum is 5 + 6 + 7 = 18 and nums = [1,2,3,4,8]
# So, we will return 18.
# It can be proven, that 18 is the maximum answer that we can achieve.
# Example 2:

# Input:
nums2 = [5,5,5]
k2 = 2
# Output: 11
# Explanation: We need to choose exactly 2 elements from nums to maximize the sum.
# For the first iteration, we choose 5. Then sum is 5 and nums = [5,5,6]
# For the second iteration, we choose 6. Then sum is 5 + 6 = 11 and nums = [5,5,7]
# So, we will return 11.
# It can be proven, that 11 is the maximum answer that we can achieve.

def maximizeSum(nums, k: int) -> int:
    m = max(nums)
    c = 0
    for i in range(k):
        c += m
        m += 1
    return c

print(maximizeSum(nums1, k1))
print(maximizeSum(nums2, k2))


def maximizeSum1(nums, k: int) -> int:
    num = max(nums)
    return (num + num + k - 1) * k // 2

print(maximizeSum1(nums1, k1))
print(maximizeSum1(nums2, k2))
