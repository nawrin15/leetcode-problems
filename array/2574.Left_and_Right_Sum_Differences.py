# Example 1:

# Input: 
nums1 = [10,4,8,3]
# Output: [15,1,11,22]
# Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
# The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
# Example 2:

# Input: 
nums2 = [1]
# Output: [0]
# Explanation: The array leftSum is [0] and the array rightSum is [0].
# The array answer is [|0 - 0|] = [0].

def leftRightDifference(nums):
    lsum, rsum = 0, sum(nums)
    for i in range(len(nums)):
        rsum -= nums[i]
        temp = abs(lsum-rsum)
        lsum += nums[i]
        nums[i] = temp
    return nums

print(leftRightDifference(nums1))
print(leftRightDifference(nums2))
