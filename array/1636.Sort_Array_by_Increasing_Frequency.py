# Example 1:

# Input: 
nums1 = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
# Example 2:

# Input: 
nums2 = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
# Example 3:

# Input: 
nums3 = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]

from collections import Counter

def frequencySort(nums):
    counter = Counter(nums)
    return sorted(nums, key=lambda x: (counter[x], -x))

print(frequencySort(nums1))
print(frequencySort(nums2))
print(frequencySort(nums3))


def frequencySort1(nums):
    counts = Counter(nums)
    pairs = []
    for key, value in counts.items():
        pairs.append((value, -key))
    pairs.sort()
    ans = []
    for times, num in pairs:
        ans += [-num] * times
    return ans

print(frequencySort1(nums1))
print(frequencySort1(nums2))
print(frequencySort1(nums3))


def frequencySort2(nums):
    count = Counter(nums)
    def sorting(num):
        return (count[num],-num)
    nums.sort(key=sorting)
    return nums

print(frequencySort2(nums1))
print(frequencySort2(nums2))
print(frequencySort2(nums3))

def frequencySort3(nums):
    freq = [0] * 201
    for x in nums:
        freq[x + 100] -= 1
    return sorted(nums, key=lambda x: (freq[x + 100], x), reverse=True)

print(frequencySort3(nums1))
print(frequencySort3(nums2))
print(frequencySort3(nums3))