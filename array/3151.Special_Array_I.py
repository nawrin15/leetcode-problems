# Example 1:

# Input: 
nums1 = [1]

# Output: true

# Explanation:

# There is only one element. So the answer is true.

# Example 2:

# Input: 
nums2 = [2,1,4]

# Output: true

# Explanation:

# There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

# Example 3:

# Input: 
nums3 = [4,3,1,6]

# Output: false

# Explanation:

# nums[1] and nums[2] are both odd. So the answer is false.

def isArraySpecial(nums) -> bool:
    check_mate = nums[0] % 2
    for i in range(1, len(nums)):
        if i % 2 == 0 and nums[i] % 2 != check_mate:
            return False
        elif i % 2 == 1 and nums[i] % 2 == check_mate:
            return False
    return True

print(isArraySpecial(nums1))
print(isArraySpecial(nums2))
print(isArraySpecial(nums3))

def isArraySpecial1(nums) -> bool:
    for i in range(len(nums) - 1):
        if (nums[i] % 2) ^ (nums[i + 1] % 2) == 0:
            return False
    return True

print(isArraySpecial1(nums1))
print(isArraySpecial1(nums2))
print(isArraySpecial1(nums3))