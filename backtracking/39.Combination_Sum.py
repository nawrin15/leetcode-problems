# Example 1:

# Input: 
candidates1 = [2,3,6,7]
target1 = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: 
candidates2 = [2,3,5] 
target2 = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# Example 3:

# Input: 
candidates3 = [2]
target3 = 1
# Output: []


def dfs(nums, target, path, res):
    if target < 0:
        return
    if target == 0:
        res.append(path)
        return
    for i in range(len(nums)):
        dfs(nums[i:], target-nums[i], path+[nums[i]], res)

def combinationSum(candidates, target):
    res = []
    dfs(candidates, target, [], res)
    return res

print(combinationSum(candidates1, target1))
print(combinationSum(candidates2, target2))
print(combinationSum(candidates3, target3))
