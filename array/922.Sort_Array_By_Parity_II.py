# Example 1:

# Input: 
nums1 = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: 
nums2 = [2,3]
# Output: [2,3]

def sortArrayByParityII(nums):
    n = len(nums)
    res = [-1] * n
    even = 0
    odd = 1
    for i in range(n):
        if nums[i] % 2 == 0:
            res[even] = nums[i]
            even += 2
        else:
            res[odd] = nums[i]
            odd += 2
    return res

print(sortArrayByParityII(nums1))  
print(sortArrayByParityII(nums2))  

def sortArrayByParityII1(nums):
    n = len(nums)
    even = 0
    odd = 1
    while even < n and odd < n:
        if nums[even] % 2 == 0:
            even += 2
        elif nums[odd] % 2 == 1:
            odd += 2
        else:
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2
    return nums

print(sortArrayByParityII1(nums1))  
print(sortArrayByParityII1(nums2)) 


