# Example 1:

# Input: 
s1 = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: 
s2 = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: 
s3 = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
s4 = "aab"
#output: 2
s5 = "dvdf"
#output: 3

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxi = pointer = 0
    seen = {}
    for i in range(len(s)):
        if s[i] in seen and seen[s[i]] >= pointer:
            pointer = seen[s[i]] + 1
        else:
            maxi = max(maxi, i - pointer + 1)
        seen[s[i]] = i
    return maxi

print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))
print(lengthOfLongestSubstring(s4))
print(lengthOfLongestSubstring(s5))

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    maxi = 0
    seen = set()
    for i in range(len(s)):
        if s[i] in seen:
            print(i, seen)
            maxi = max(maxi, len(seen))
            seen = set(s[i])
        else:
            seen.add(s[i])
    maxi = max(maxi, len(seen))
    return maxi

print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))
print(lengthOfLongestSubstring(s4))
print(lengthOfLongestSubstring(s5))
