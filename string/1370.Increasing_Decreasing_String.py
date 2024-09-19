# Example 1:

# Input: 
s1 = "aaaabbbbcccc"
# Output: "abccbaabccba"
# Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
# After steps 4, 5 and 6 of the first iteration, result = "abccba"
# First iteration is done. Now s = "aabbcc" and we go back to step 1
# After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
# After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
# Example 2:

# Input: 
s2 = "rat"
# Output: "art"
# Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.
s3 = "aaaabbbbcccc"
#output: "abccbaabccba"

from collections import defaultdict, Counter

def sortString(s: str) -> str:
    frequency = defaultdict(int)
    res = ""
    for i in s:
        frequency[ord(i)-97] += 1
    n = len(s)
    while n > 0:
        for i in range(26):
            if frequency[i] > 0:
                frequency[i] -= 1
                n -= 1
                res += chr(i+97)
        for i in range(26, -1, -1):
            if frequency[i] > 0:
                frequency[i] -= 1
                n -= 1
                res += chr(i+97) 
    return res

print(sortString(s1))     
print(sortString(s2))   
print(sortString(s3))   

import string 

def sortString1(s: str) -> str:
    s_map = Counter(s)
    res = []
    asc = True
    while len(res) < len(s):
        for i in range(26):
            c = string.ascii_lowercase[i if asc else ~i]
            if s_map[c] > 0:
                res.append(c)
                s_map[c] -= 1
        asc = not asc
    return ''.join(res)

print(sortString1(s1))     
print(sortString1(s2))   
print(sortString1(s3))   

def sortString2(s: str) -> str:
    s = list(s)
    result = ''
    while s:
        for letter in sorted(set(s)):
            s.remove(letter)
            result += letter
        for letter in sorted(set(s), reverse=True):
            s.remove(letter)
            result += letter
    return result

print(sortString2(s1))     
print(sortString2(s2))   
print(sortString2(s3))   



