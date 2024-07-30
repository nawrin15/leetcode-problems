# Example 1:

# Input: 
nums1 = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# Example 2:

# Input: 
nums2 = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
from collections import defaultdict


##solution 1
def backtrack(result, tempList, nums, visited):
    if len(tempList) == len(nums) and not (tempList[:] in result):
        result.append(tempList[:])
        return 
    for i in range(len(nums)):
        num = nums[i]
        if visited[i]:
            continue
        visited[i] = True
        tempList.append(num)
        backtrack(result, tempList, nums, visited)
        tempList.pop()
        visited[i] = False
    return 

def permuteUnique1(nums):
    result = []
    visited = [False] * len(nums)
    backtrack(result, [], nums, visited)
    return result

print(permuteUnique1(nums1))
print(permuteUnique1(nums2))
##solution 2
from collections import Counter

def permuteUnique2(nums):
    result = []
    d = Counter(nums)
    print(d)
    def dfs(path):
        if len(path) == len(nums):
            result.append(path.copy())
            return

        #To avoid duplicates we need to only iterate through elements in the dictionary
        
        for num in d:
            if d[num] > 0:
                d[num] -= 1
                path.append(num)
                dfs(path)
                d[num] += 1
                path.pop()

    dfs([])
    return result

print(permuteUnique2(nums1))
print(permuteUnique2(nums2))
##Solution 3
from itertools import permutations
def permuteUnique3(nums):
    return set(permutations(nums)) 



print(permuteUnique3(nums1))
print(permuteUnique3(nums2))

