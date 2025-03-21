# Example 1:

# Input: 
nums1 = [3,2,2,3]
val1 = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: 
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).


def removeElement(nums, val: int) -> int:
    j = 0
    for i in range(len(nums)):
        if val != nums[i]:
            nums[j] = nums[i]
            j += 1
    return j 

print(removeElement(nums1, val1))
print(removeElement(nums2, val2))