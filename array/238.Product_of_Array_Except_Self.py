#### 238. Product of Array Except Self

nums = [1,2,3,4]

ans = [1]* len(nums)
prev = 1
for i in range(len(nums)):
    ans[i] = prev
    prev *= nums[i]
    
prev = 1
for i in range(len(nums)-1, -1, -1):
    ans[i] *= prev
    prev *= nums[i]
    
print(ans)