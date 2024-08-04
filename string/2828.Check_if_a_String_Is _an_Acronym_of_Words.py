# Example 1:

# Input: 
words1 = ["alice","bob","charlie"]
s1 = "abc"
# Output: true
# Explanation: The first character in the words "alice", "bob", and "charlie" are 'a', 'b', and 'c', respectively. Hence, s = "abc" is the acronym. 
# Example 2:

# Input: 
words2 = ["an","apple"]
s2 = "a"
# Output: false
# Explanation: The first character in the words "an" and "apple" are 'a' and 'a', respectively. 
# The acronym formed by concatenating these characters is "aa". 
# Hence, s = "a" is not the acronym.
# Example 3:

# Input: 
words3 = ["never","gonna","give","up","on","you"]
s3 = "ngguoy"
# Output: true
# Explanation: By concatenating the first character of the words in the array, we get the string "ngguoy". 
# Hence, s = "ngguoy" is the acronym.

def isAcronym(words, s: str) -> bool:
    if len(words) != len(s):
        return False
    for i in range(len(s)):
        word = words[i]
        if word[0] != s[i]:
            return False
    return True

print(isAcronym(words1, s1))
print(isAcronym(words2, s2))
print(isAcronym(words3, s3))

def isAcronym(words, s: str) -> bool:
    return ''.join([word[0] for word in words]) == s

print(isAcronym(words1, s1))
print(isAcronym(words2, s2))
print(isAcronym(words3, s3))