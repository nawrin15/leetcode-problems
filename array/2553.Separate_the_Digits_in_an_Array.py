# Example 1:

# Input: 
nums1 = [13,25,83,77]
# Output: [1,3,2,5,8,3,7,7]
# Explanation: 
# - The separation of 13 is [1,3].
# - The separation of 25 is [2,5].
# - The separation of 83 is [8,3].
# - The separation of 77 is [7,7].
# answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
# Example 2:

# Input: 
nums2 = [7,1,3,9]
# Output: [7,1,3,9]
# Explanation: The separation of each integer in nums is itself.
# answer = [7,1,3,9].

def separateDigits(nums):
    res = []
    for num in nums:
        temp = []
        while num != 0:
            temp.append(num % 10)
            num //= 10
        temp.reverse()
        res.extend(temp)
    return res

print(separateDigits(nums1))
print(separateDigits(nums2))

def separateDigits1(nums):
    res = []
    for num in nums[::-1]:
        while num:
            res.append(num % 10)
            num //= 10
    return res[::-1]

print(separateDigits1(nums1))
print(separateDigits1(nums2))


def separateDigits2(nums):
    return [int(n) for num in nums for n in str(num)]

print(separateDigits2(nums1))
print(separateDigits2(nums2))