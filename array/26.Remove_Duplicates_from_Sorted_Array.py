nums1 = [1,1,2]
#Output: 2

nums2 = [0,0,1,1,1,2,2,3,3,4]
#Output: 5


def removeDuplicates1(nums) -> int:
    j = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j

print(removeDuplicates1(nums1))
print(removeDuplicates1(nums2))

def removeDuplicates2(nums) -> int:
        nums[:] = sorted(set(nums))
        print(nums)
        return len(nums)


print(removeDuplicates2(nums1))
print(removeDuplicates2(nums2))