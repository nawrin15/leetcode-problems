from collections import defaultdict 

class Solution:
    def init_value(self):
        return 0

    def fourSumCount1(self, nums1, nums2, nums3, nums4) -> int:
        map = defaultdict(self.init_value)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                map[nums1[i]+nums2[j]] += 1
        count = 0
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                target = -(nums3[k] + nums4[l])
                if target in map:
                    count += map[target]

        return count
    
    def fourSumCount2(self, nums1, nums2, nums3, nums4) -> int:
        map = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                target = nums1[i]+nums2[j]
                map[target] = map.get(target, 1)
        count = 0
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                target = -(nums3[k] + nums4[l])
                if target in map:
                    count += map[target]

        return count

a = Solution()

#Example 1:

#Input: 
nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
print(a.fourSumCount1(nums1, nums2, nums3, nums4))
print(a.fourSumCount2(nums1, nums2, nums3, nums4))
#Output: 2
#Explanation:
#The two tuples are:
#1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
#2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0


#Example 2:

#Input: 
nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
print(a.fourSumCount1(nums1, nums2, nums3, nums4))
print(a.fourSumCount2(nums1, nums2, nums3, nums4))
#Output: 1