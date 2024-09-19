# Example 1:

# Input: 
words1 = ["a","b","c","ab","bc","abc"]
s1 = "abc"
# Output: 3
# Explanation:
# The strings in words which are a prefix of s = "abc" are:
# "a", "ab", and "abc".
# Thus the number of strings in words which are a prefix of s is 3.
# Example 2:

# Input: 
words2 = ["a","a"]
s2 = "aa"
# Output: 2
# Explanation:
# Both of the strings are a prefix of s. 
# Note that the same string can occur multiple times in words, and it should be counted each time.

def countPrefixes(words, s: str) -> int:
    return sum(1 for word in words if word == s[:len(word)])

print(countPrefixes(words1, s1))
print(countPrefixes(words2, s2))

def countPrefixes1(words, s: str) -> int:
    return len([1 for word in words if word == s[:len(word)]])

print(countPrefixes1(words1, s1))
print(countPrefixes1(words2, s2))

def countPrefixes2(words, s: str) -> int:
    return sum(1 for word in words if s.startswith(word))

print(countPrefixes2(words1, s1))
print(countPrefixes2(words2, s2))