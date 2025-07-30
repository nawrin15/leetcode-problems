# Example 1:

# Input: 
strs1 = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: 
strs2 = [""]

# Output: [[""]]

# Example 3:

# Input: 
strs3 = ["a"]

# Output: [["a"]]

from collections import defaultdict

def groupAnagrams(strs):
    letter_dicts = defaultdict(list)
    for word in strs:
        letter_dicts["".join(sorted(word))].append(word)
    return list(letter_dicts.values())

print(groupAnagrams(strs1))
print(groupAnagrams(strs2))
print(groupAnagrams(strs3))

def groupAnagrams(strs):
    letter_dicts = {}
    for word in strs:
        m = "".join(sorted(word))
        if m not in letter_dicts:
            letter_dicts[m] = [word]
        else:
            letter_dicts[m].append(word)
    return list(letter_dicts.values())

print(groupAnagrams(strs1))
print(groupAnagrams(strs2))
print(groupAnagrams(strs3))