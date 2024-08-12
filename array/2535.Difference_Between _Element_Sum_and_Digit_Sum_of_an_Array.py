# Example 1:

# Input: 
nums1 = [1,15,6,3]
# Output: 9
# Explanation: 
# The element sum of nums is 1 + 15 + 6 + 3 = 25.
# The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
# The absolute difference between the element sum and digit sum is |25 - 16| = 9.
# Example 2:

# Input: 
nums2 = [1,2,3,4]
# Output: 0
# Explanation:
# The element sum of nums is 1 + 2 + 3 + 4 = 10.
# The digit sum of nums is 1 + 2 + 3 + 4 = 10.
# The absolute difference between the element sum and digit sum is |10 - 10| = 0.

def differenceOfSum(nums) -> int:
    esum = sum(nums)
    dsum = 0
    for num in nums:
        while num != 0:
            dsum += num % 10
            num = num // 10

    return abs(esum - dsum)

print(differenceOfSum(nums1))
print(differenceOfSum(nums2))

def differenceOfSum2(nums) -> int:
    esum = sum(nums)
    dsum = 0
    for num in nums:
        for d in str(num):
            dsum += int(d)
    return abs(esum - dsum)

print(differenceOfSum2(nums1))
print(differenceOfSum2(nums2))