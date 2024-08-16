# Example 1:

# Input: 
words1 = ["pay","attention","practice","attend"]
pref1 = "at"
# Output: 2
# Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
# Example 2:

# Input: 
words2 = ["leetcode","win","loops","success"]
pref2 = "code"
# Output: 0
# Explanation: There are no strings that contain "code" as a prefix.

def prefixCount(words, pref: str) -> int:
    n = len(pref)
    return sum(1 for word in words if word[:n] == pref) 
        

print(prefixCount(words1, pref1))
print(prefixCount(words2, pref2))

def prefixCount1(words, pref: str) -> int:
    res = 0
    for word in words:
        if word.startswith(pref):
            res += 1
    return res 
        

print(prefixCount1(words1, pref1))
print(prefixCount1(words2, pref2))