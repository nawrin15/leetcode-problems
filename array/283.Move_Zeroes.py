###283. Move Zeroes

nums = [7, 8, 9, 0,0,1,0, 0, 3,12, 0, 7]
pointer = 0

for i in range(len(nums)):
    if nums[i] != 0:
        if nums[pointer] == 0:
            nums[i], nums[pointer] = nums[pointer], nums[i]
        pointer += 1
        
print(nums)