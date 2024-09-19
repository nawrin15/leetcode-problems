# Example 1:

# Input: 
arr1 = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: 
arr2 = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

def replaceElements(arr):
    maxi = -1
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxi
        maxi = max(temp, maxi)
    return arr

print(replaceElements(arr1))
print(replaceElements(arr2))
