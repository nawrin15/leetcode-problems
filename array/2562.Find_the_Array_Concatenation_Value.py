# Example 1:

# Input: 
nums1 = [7,52,2,4]
# Output: 596
# Explanation: Before performing any operation, nums is [7,52,2,4] and concatenation value is 0.
#  - In the first operation:
# We pick the first element, 7, and the last element, 4.
# Their concatenation is 74, and we add it to the concatenation value, so it becomes equal to 74.
# Then we delete them from nums, so nums becomes equal to [52,2].
#  - In the second operation:
# We pick the first element, 52, and the last element, 2.
# Their concatenation is 522, and we add it to the concatenation value, so it becomes equal to 596.
# Then we delete them from the nums, so nums becomes empty.
# Since the concatenation value is 596 so the answer is 596.
# Example 2:

# Input: 
nums2 = [5,14,13,8,12]
# Output: 673
# Explanation: Before performing any operation, nums is [5,14,13,8,12] and concatenation value is 0.
#  - In the first operation:
# We pick the first element, 5, and the last element, 12.
# Their concatenation is 512, and we add it to the concatenation value, so it becomes equal to 512.
# Then we delete them from the nums, so nums becomes equal to [14,13,8].
#  - In the second operation:
# We pick the first element, 14, and the last element, 8.
# Their concatenation is 148, and we add it to the concatenation value, so it becomes equal to 660.
# Then we delete them from the nums, so nums becomes equal to [13].
#  - In the third operation:
# nums has only one element, so we pick 13 and add it to the concatenation value, so it becomes equal to 673.
# Then we delete it from nums, so nums become empty.
# Since the concatenation value is 673 so the answer is 673.

def findTheArrayConcVal(nums) -> int:
    n = len(nums)
    res = 0
    for i in range(n//2):
        res += int(str(nums[i]) + str(nums[n-i-1]))
    if n % 2 == 1:
        res += nums[n//2]
    return res

print(findTheArrayConcVal(nums1))
print(findTheArrayConcVal(nums2))

def findTheArrayConcVal(nums) -> int:
    left, right = 0, len(nums) - 1
    res = 0
    while left < right:
        res += int(str(nums[left]) + str(nums[right]))
        left += 1
        right -= 1
    if left == right:
        res += nums[left]
    return res

print(findTheArrayConcVal(nums1))
print(findTheArrayConcVal(nums2))