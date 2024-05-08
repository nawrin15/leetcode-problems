# Brute force solution but time limit exceed T(O):n^3

class Solution:
    def threeSum1(self, nums):
        n = len(nums)
        sets = []
        triplets = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0 :
                        triplets = sorted([nums[i], nums[j], nums[k]])
                        if triplets not in sets:
                            sets.append(triplets)
        return sets
    
    def threeSum2(self, nums):
        n = len(nums)
        sets = []
        for i in range(n):
            hash_map = set()
            for j in range(i + 1, n):
                required_sum = -(nums[i] + nums[j])
                if required_sum in hash_map:
                    triplets = sorted([nums[i], nums[j], required_sum])
                    if triplets not in sets:
                        sets.append(triplets)
                hash_map.add(nums[j])
        return sets

    def threeSum3(self, nums):
        n = len(nums)
        nums = sorted(nums)
        sets = []
        for i in range(n):
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    sets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]: j += 1
                    while j < k and nums[k] == nums[k + 1]: k -=1

        
        return sets

a =Solution()

#Example 1:
#Input: 
nums1 = [-1,0,1,2,-1,-4]
print(a.threeSum1(nums1))
print(a.threeSum2(nums1))
print(a.threeSum3(nums1))
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation: 
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2].
#Notice that the order of the output and the order of the triplets does not matter.


#Example 2:
#Input: 
nums2 = [0,1,1]
print(a.threeSum1(nums2))
print(a.threeSum2(nums2))
print(a.threeSum3(nums2))
#Output: []
#Explanation: The only possible triplet does not sum up to 0.

#Example 3:
#Input: 
nums3 = [0,0,0]
print(a.threeSum1(nums3))
print(a.threeSum2(nums3))
print(a.threeSum3(nums3))
#Output: [[0,0,0]]
#Explanation: The only possible triplet sums up to 0.
 