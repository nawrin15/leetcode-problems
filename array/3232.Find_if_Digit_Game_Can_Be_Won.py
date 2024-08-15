# Example 1:

# Input: 
nums1 = [1,2,3,4,10]

# Output: false

# Explanation:

# Alice cannot win by choosing either single-digit or double-digit numbers.

# Example 2:

# Input: 
nums2 = [1,2,3,4,5,14]

# Output: true

# Explanation:

# Alice can win by choosing single-digit numbers which have a sum equal to 15.

# Example 3:

# Input: 
nums3 = [5,5,5,25]

# Output: true

# Explanation:

# Alice can win by choosing double-digit numbers which have a sum equal to 25.

def canAliceWin(nums) -> bool:
    return sum(num if num < 10 else -num for num in nums) != 0

print(canAliceWin(nums1))
print(canAliceWin(nums2))
print(canAliceWin(nums3))

def canAliceWin1(nums) -> bool:
    sum1 = sum2 = 0
    for num in nums:
        if num < 10:
            sum1 += num
        else:
            sum2 += num 
    return sum1 != sum2

print(canAliceWin1(nums1))
print(canAliceWin1(nums2))
print(canAliceWin1(nums3))