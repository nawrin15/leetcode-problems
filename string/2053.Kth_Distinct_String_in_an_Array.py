# Example 1:

# Input: 
arr1 = ["d","b","c","b","c","a"]
k1 = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1st, so it is the 1st distinct string.
# "a" appears 2nd, so it is the 2nd distinct string.
# Since k == 2, "a" is returned. 
# Example 2:

# Input: 
arr2 = ["aaa","aa","a"]
k2 = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1st string "aaa" is returned.
# Example 3:

# Input: 
arr3 = ["a","b","a"]
k3 = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".

from collections import Counter

def kthDistinct(arr, k: int) -> str:
        order = 0
        counter = Counter(arr)
        for i in arr:
            if counter[i] == 1:
                order += 1
            if order == k:
                 return i
        return ""

print(kthDistinct(arr1, k1))
print(kthDistinct(arr2, k2))
print(kthDistinct(arr3, k3))