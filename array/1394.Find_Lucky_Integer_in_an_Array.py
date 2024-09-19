# Example 1:

# Input: 
arr1 = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:

# Input: 
arr2 = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:

# Input: 
arr3 = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.

from collections import Counter, defaultdict

def findLucky(arr) -> int:
    count = Counter(arr)
    lucky = -1
    for i in count:
        if i == count[i]:
            if i > lucky:
                lucky = i
    return -1 if lucky == -1 else count[lucky]

print(findLucky(arr1))
print(findLucky(arr2))
print(findLucky(arr3))

def findLucky1(arr) -> int:
    freq = defaultdict(int)
    for num in arr:
        freq[num] += 1 
    lucky = -1
    for i in freq:
        if i == freq[i]:
            lucky = max(lucky, freq[i])
    return lucky

print(findLucky1(arr1))
print(findLucky1(arr2))
print(findLucky1(arr3))
