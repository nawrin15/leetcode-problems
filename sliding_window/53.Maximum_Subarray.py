# Example 1:

# Input: 
nums1 = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: 
nums2 = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: 
nums3 = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
##kadane's Algorithm
def maxSubArray1(nums):
    maxSum = nums[0]
    currSum = nums[0]
    for i in range(1, len(nums)):
        currSum = max(nums[i], currSum + nums[i])
        maxSum = max(maxSum, currSum) 
    return maxSum

print(maxSubArray1(nums1))
print(maxSubArray1(nums2))
print(maxSubArray1(nums3))

def maxSubArray2(nums):
    maxSum = nums[0]
    currSum = 0
    for n in nums:
        if currSum < 0:
            currSum = 0
        currSum += n
        maxSum = max(maxSum, currSum) 
    return maxSum

print(maxSubArray2(nums1))
print(maxSubArray2(nums2))
print(maxSubArray2(nums3))

