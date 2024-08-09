# Example 1:

# Input: 
nums1 = [1,2,3,4]

# Output: 3

# Explanation:

# All array elements can be made divisible by 3 using 3 operations:

# Subtract 1 from 1.
# Add 1 to 2.
# Subtract 1 from 4.
# Example 2:

# Input: 
nums2 = [3,6,9]

# Output: 0

def minimumOperations(nums) -> int:
    res = 0
    for num in nums:
        if num % 3 != 0:
            res += 1
    return res

print(minimumOperations(nums1))
print(minimumOperations(nums2))

def minimumOperations1(nums) -> int:
    return sum([0 if num % 3 == 0 else 1 for num in nums])


print(minimumOperations1(nums1))
print(minimumOperations1(nums2))