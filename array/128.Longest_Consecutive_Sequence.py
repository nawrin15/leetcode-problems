# Example 1:

# Input: 
nums1 = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: 
nums2 = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Input: 
nums3 = []
# Output: 0

# Input: 
nums4 = [0]
# Output: 1

# Input: 
nums5 = [1,2,0,1]
# Output: 3

# Input: 
nums6 = [9,1,4,7,3,-1,0,5,8,-1,6]
# Output: 7



# time complixity - nlogn
def longestConsecutive(nums) -> int:
    nums = sorted(set(nums))
    n = len(nums)
    count = 1
    maxi = 1
    if n == 0:
        return 0
    prev = nums[0]
    for i in range(1, n):
        if prev + 1 == nums[i]:
            count += 1
        else:
            maxi = max(maxi, count)
            count = 1
        prev = nums[i]
        maxi = max(maxi, count)
    return maxi

# print(longestConsecutive(nums1))
# print(longestConsecutive(nums2))
# print(longestConsecutive(nums3))
# print(longestConsecutive(nums4))
# print(longestConsecutive(nums5))
    
        
# time complixity - nlogn
def longestConsecutive(nums) -> int:
    nums = sorted(set(nums))
    n = len(nums)
    count = 1
    maxi = 1
    if n == 0:
        return 0
    for i in range(1, n):
        if nums[i] - nums[i - 1] == 1:
            count += 1
        elif nums[i] == nums[i - 1]:
            continue
        else:
            maxi = max(maxi, count)
            count = 1
        maxi = max(maxi, count)
    return maxi

# print(longestConsecutive(nums1))
# print(longestConsecutive(nums2))
# print(longestConsecutive(nums3))
# print(longestConsecutive(nums4))
# print(longestConsecutive(nums5))

# time complixity - nlogn
def longestConsecutive(nums) -> int:
    nums = sorted(set(nums))
    n = len(nums)
    count = 1
    maxi = 1
    if n == 0:
        return 0
    for i in range(1, n):
        if nums[i] - nums[i - 1] == 1:
            count += 1
        elif nums[i] == nums[i - 1]:
            continue
        else:
            maxi = max(maxi, count)
            count = 1
        maxi = max(maxi, count)
    return maxi

# print(longestConsecutive(nums1))
# print(longestConsecutive(nums2))
# print(longestConsecutive(nums3))
# print(longestConsecutive(nums4))
# print(longestConsecutive(nums5))
        
from collections import defaultdict

#[9,1,4,7,3,-1,0,5,8,-1,6] -1, 0, 1   3, 4, 5, 6, 7,8, 9


# time complixity - n
def longestConsecutive(nums) -> int:
    d = defaultdict()
    if len(nums) < 1: return 0
    for num in nums:
        d[num] = False
    maxi = 1
    res_all = []
    for num in nums:
        if d[num]:
            continue
        count = 1
        d[num] = True
        actual = num
        res = []
        res.append(num)
        while (num + 1) in d:
            d[num + 1] = True
            count += 1
            num += 1
            res.append(num)
        num = actual
        while num - 1 in d:
            d[num - 1] = True
            num -= 1
            count += 1
            res.append(num)
        maxi = max(maxi, count)
        res_all.append(res)
    print(res_all)
    return maxi

print(longestConsecutive(nums1))
print(longestConsecutive(nums2))
print(longestConsecutive(nums3))
print(longestConsecutive(nums4))
print(longestConsecutive(nums5))
print(longestConsecutive(nums6))

# time complixity - n
def longestConsecutive(nums) -> int:
    d = defaultdict()
    if len(nums) < 1: return 0
    for num in nums:
        d[num] = False
    maxi = 1
    for num in nums:
        if d[num]:
            continue
        count = 1
        d[num] = True
        inc = num + 1
        while inc in d:
            d[inc] = True
            count += 1
            inc += 1
        dec = num - 1
        while dec in d:
            d[dec] = True
            count += 1
            dec -= 1
        maxi = max(maxi, count)
    return maxi

print(longestConsecutive(nums1))
print(longestConsecutive(nums2))
print(longestConsecutive(nums3))
print(longestConsecutive(nums4))
print(longestConsecutive(nums5))
print(longestConsecutive(nums6))


# time complixity - n
def longestConsecutive(nums) -> int:
    if len(nums) < 1: return 0
    nums = set(nums)
    used = set()
    maxi = 1
    for num in nums:
        if num in used:
            continue
        count = 1
        used.add(num)
        inc = num + 1
        while inc in nums:
            used.add(inc)
            count += 1
            inc += 1
        dec = num - 1
        while dec in nums:
            used.add(dec)
            count += 1
            dec -= 1
        maxi = max(maxi, count)
    return maxi

print(longestConsecutive(nums1))
print(longestConsecutive(nums2))
print(longestConsecutive(nums3))
print(longestConsecutive(nums4))
print(longestConsecutive(nums5))
print(longestConsecutive(nums6))