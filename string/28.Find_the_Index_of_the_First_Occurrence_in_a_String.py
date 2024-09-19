# Example 1:

# Input: 
haystack1 = "sadbutsad"
needle1 = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: 
haystack2 = "leetcode"
needle2 = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

haystack3 = "aaa"
needle3 = "aaa"

haystack4 = "mississippi"
needle4 = "issip"

def strStr(haystack: str, needle: str) -> int:
    m = len(needle)
    n = len(haystack)
    for i in range(n - m + 1):
        if haystack[i:i+m] == needle:
            return i
    return -1

print(strStr(haystack1, needle1))
print(strStr(haystack2, needle2))
print(strStr(haystack3, needle3))
print(strStr(haystack4, needle4))