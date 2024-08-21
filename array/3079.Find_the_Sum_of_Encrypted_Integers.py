# Example 1:

# Input: 
nums1 = [1,2,3]

# Output: 6

# Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.

# Example 2:

# Input: 
nums2 = [10,21,31]

# Output: 66

# Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.
nums3 = [109]
#output:999

def sumOfEncryptedInt(nums) -> int:
    res = 0
    for num in nums:
        num = str(num)
        res += int(str(max(list(num))) * len(num))
    return res

print(sumOfEncryptedInt(nums1))
print(sumOfEncryptedInt(nums2))

def sumOfEncryptedInt1(nums) -> int:
    return sum(int(str(max(list(str(num)))) * len(str(num))) for num in nums)

print(sumOfEncryptedInt1(nums1))
print(sumOfEncryptedInt1(nums2))

def sumOfEncryptedInt2(nums) -> int:
    res = 0
    for num in nums:
        count = 0
        maxi = -1
        while num != 0:
            maxi = max(maxi, num % 10)
            num = num // 10
            count += 1
        n = 0
        for i in range(count):
            n += 10**i * maxi
        res += n
    return res
             
print(sumOfEncryptedInt2(nums1))
print(sumOfEncryptedInt2(nums2))
print(sumOfEncryptedInt2(nums3))

def sumOfEncryptedInt3(nums) -> int:
    def make_max(num):
        times = _max = 0
        while num > 0:
            _max = max(_max,num%10)
            num //= 10
            times = times*10 + 1
        return _max * times
    total = 0
    for num in nums:
        total += make_max(num)
    return total
            
print(sumOfEncryptedInt3(nums1))
print(sumOfEncryptedInt3(nums2))
print(sumOfEncryptedInt3(nums3))