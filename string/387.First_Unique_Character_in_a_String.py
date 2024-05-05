from collections import defaultdict 

s1 = "leetcode"
# Output: 0

s2 = "loveleetcode"
# Output: 2

s3 = "aabb"
# Output: -1

def firstUniqChar(s: str) -> int:
    count = defaultdict(int)
    for char in s:
        count[char] = count[char] + 1
        
    for index, char in enumerate(s):
        if count[char] == 1: return index
    return -1

print(firstUniqChar(s1))
print(firstUniqChar(s2))
print(firstUniqChar(s3))