# Example 1:

# Input: 
arr1a = [2,3,1,3,2,4,6,7,9,2,19]
arr2a = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]
# Example 2:

# Input: 
arr1b = [28,6,22,8,44,17]
arr2b = [22,28,8,6]
# Output: [22,28,8,6,17,44]

from collections import defaultdict

def relativeSortArray(arr1, arr2):
    arr2_set = set(arr2)
    extra = []
    res = []
    count = defaultdict(int)
    for num in arr1:
        if num not in arr2_set:
            extra.append(num)
        else:
            count[num] += 1
    for num in arr2:
        for i in range(count[num]):
            res.append(num)
    return res + sorted(extra)

print(relativeSortArray(arr1a, arr2a))
print(relativeSortArray(arr1b, arr2b))


def relativeSortArray1(arr1, arr2):
    arr2_set = set(arr2)
    extra = []
    res = []
    count = defaultdict(int)
    for num in arr1:
        if num not in arr2_set:
            extra.append(num)
        else:
            count[num] += 1
    for num in arr2:
            res.extend([num] * count[num])
    return res + sorted(extra)

print(relativeSortArray1(arr1a, arr2a))
print(relativeSortArray1(arr1b, arr2b))