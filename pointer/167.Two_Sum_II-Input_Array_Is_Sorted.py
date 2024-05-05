class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []


numbers = [2,7,11,15]
target = 9
a = Solution() 
#Output: [1,2]
print(a.twoSum(numbers, target))

numbers = [2,3,4]
target = 6
a = Solution()
#Output: [1,3]
print(a.twoSum(numbers, target))


numbers = [-1,0]
target = -1
a = Solution()
#Output: [1,2]
print(a.twoSum(numbers, target))