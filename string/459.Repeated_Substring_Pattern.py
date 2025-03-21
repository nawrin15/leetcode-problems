# Example 1:

# Input: 
s1 = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: 
s2 = "aba"
# Output: false
# Example 3:

# Input:
s3 = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
s4 = "babbabbabbabbab"
#output: True
s5 = "ababab"
#output: True

def repeatedSubstringPattern(s: str) -> bool:
    n = len(s)
    if n % 2 == 1:
        return False
    for i in range(1, n//2+1):
        if n % i == 0:
            if s[:i] * (n // i) == s:
                return True
    return False


print(repeatedSubstringPattern(s1))
print(repeatedSubstringPattern(s2))
print(repeatedSubstringPattern(s3))
print(repeatedSubstringPattern(s4))
print(repeatedSubstringPattern(s5))


def repeatedSubstringPattern(s: str) -> bool:
    n = len(s)
    if n == 1: return False
    ss = s + s
    print(ss[1:-1])
    return s in ss[1:-1]


print(repeatedSubstringPattern(s1))
print(repeatedSubstringPattern(s2))
print(repeatedSubstringPattern(s3))
print(repeatedSubstringPattern(s4))
print(repeatedSubstringPattern(s5))

def repeatedSubstringPattern(s: str) -> bool:
    for i in range(1, len(s) // 2 + 1):
        pattern = s[:i]
        sub = ""
        while len(sub) <= len(s):
            sub += pattern
            if sub == s:
                return True
    return False


print(repeatedSubstringPattern(s1))
print(repeatedSubstringPattern(s2))
print(repeatedSubstringPattern(s3))
print(repeatedSubstringPattern(s4))
print(repeatedSubstringPattern(s5))