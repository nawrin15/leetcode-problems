#643. Maximum Average Subarray I 


#Naive solution - time-complexity:O(n*k)
# problem- timelimit exceed 
from typing import List

def badMaxSubArray(nums: List[int], k: int) -> int:
    max_res = float('-inf')
    for i in range(len(nums)):
        windowSum = 0
        for j in range(k):    
            if (i+k-1) < len(nums):
                windowSum += nums[i+j]
            else:
                i = len(nums)
                j = k
        max_res = max(max_res, windowSum/k)
    return round(max_res, 5)
        
        
print(badMaxSubArray([1,12,-5,-6,50,3], 4))

#Optimize solution - time-complexity:O(n)

def maxSubArray(nums: List[int], k: int) -> int:
    max_res = float('-inf')
    windowSum = 0
    start = 0
    for end in range(len(nums)):
        windowSum += nums[end]
        if (end - start +1) == k:
            max_res = max(max_res, windowSum/k)
            windowSum -= nums[start]
            start += 1
    return round(max_res, 5)


print(maxSubArray([1,12,-5,-6,50,3], 4))

# More optimize solution - time-complexity: O(n)

def maxSubArray2(nums: List[int], k: int) -> int:
    windowSum = sum(nums[:k])
    max_res = windowSum / k
    i = 0
    while (i + k + 1) <= len(nums):
        windowSum -= nums[i]
        windowSum += nums[i + k]
        max_res = max(max_res, windowSum / k)
        i += 1
        
    return round(max_res, 5)


print(maxSubArray2([1,12,-5,-6,50,3], 4))