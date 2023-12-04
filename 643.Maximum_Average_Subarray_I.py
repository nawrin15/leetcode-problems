#643. Maximum Average Subarray I
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