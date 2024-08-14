# Example 1:

# Input: 
arr1 = [3,0,1,1,9,7]
a1 = 7
b1 = 2
c1 = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
# Example 2:

# Input: 
arr2 = [1,1,2,2,3]
a2 = 0
b2 = 0
c2 = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.

def countGoodTriplets(arr, a: int, b: int, c: int) -> int:
    count = 0
    n = len(arr)
    for i in range(n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1
    return count

print(countGoodTriplets(arr1, a1, b1, c1))
print(countGoodTriplets(arr2, a2, b2, c2))

def countGoodTriplets1(arr, a: int, b: int, c: int) -> int:
    count = 0
    n = len(arr)
    for i in range(n-2):
        for j in range(i + 1, n-1):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
    return count

print(countGoodTriplets1(arr1, a1, b1, c1))
print(countGoodTriplets1(arr2, a2, b2, c2))