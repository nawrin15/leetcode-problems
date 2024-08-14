# Example 1:

# Input: 
nums1 = [0,1,4,6,7,10]
diff1 = 3
# Output: 2
# Explanation:
# (1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
# (2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3. 
# Example 2:

# Input: 
nums2 = [4,5,6,7,8,9]
diff2 = 2
# Output: 2
# Explanation:
# (0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
# (1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.

def arithmeticTriplets(nums, diff: int) -> int:
    count = 0
    n = len(nums)
    for i in range(n-2):
        for j in range(n-1):
            for k in range(n):
                if ((nums[j] - nums[i]) == diff) and ((nums[k] - nums[j]) == diff):
                    count += 1
    return count

print(arithmeticTriplets(nums1, diff1))
print(arithmeticTriplets(nums2, diff2))