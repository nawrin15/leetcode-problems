### solution -1 (one-line)
nums = [4,3,2,7,8,2,3,1]
print(set(range(1, len(nums) + 1)) - set(nums))

### solution - 2
# Time complexity : O(n)
# Space complexity : O(n)
allNums = [0] * len(nums)
print(allNums)
for i in nums:
	allNums[i - 1] = i

print([i + 1 for i in range(len(allNums)) if allNums[i] == 0])


### solution - 3
# Time complexity : O(n)
# Space complexity : O(1)

for i in nums:
    nums[abs(i) - 1]  = -abs(nums[abs(i) - 1])

print([i + 1 for i in range(len(nums)) if nums[i] > 0])
    

