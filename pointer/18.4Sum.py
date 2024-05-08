# Brute force solution but time limit exceed T(O):n^3

class Solution:

    def fourSum(self, nums, target):
        n = len(nums)
        nums = sorted(nums)
        sets = []
        for i in range(n):
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            for j in range(i+1, n):
                if j != (i + 1) and (nums[j] == nums[j-1]):
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum < target:
                        k += 1
                    elif sum > target:
                        l -= 1
                    else:
                        sets.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]: k += 1
                        while k < l and nums[l] == nums[l + 1]: l -=1

        
        return sets

a =Solution()

#Example 1:

#Input: 
nums = [1,0,-1,0,-2,2]
target = 0
#Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(a.fourSum(nums, target))
#Example 2:

#Input: 
nums = [2,2,2,2,2]
target = 8
print(a.fourSum(nums, target))

#Output: [[2,2,2,2]]
 