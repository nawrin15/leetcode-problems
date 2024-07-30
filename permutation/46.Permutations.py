# Example 1:

# Input: 
nums1 = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: 
nums2 = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: 
nums3 = [1]
# Output: [[1]]


def backtrack(result, tempList, nums):
    if len(tempList) == len(nums):
        result.append(tempList[:])
        return 
    for num in nums:
        if num in tempList:
            continue
        tempList.append(num)
        backtrack(result, tempList, nums)
        tempList.pop()

    return 

def permute(nums):
    result = []

    backtrack(result, [], nums)
    return result

print(permute(nums1))
print(permute(nums2))
print(permute(nums3))