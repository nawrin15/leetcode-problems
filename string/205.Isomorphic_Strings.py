s1 = "egg"
t1 = "add"
# Output: true

s2 = "foo"
t2 = "bar"
# Output: false

s3 = "paper"
t3 = "title"
# Output: true

s4 = "badc"
t4 = "baba"
# Output: False

def isIsomorphic(s: str, t: str) -> bool:
    map_A = {}
    map_B = {}
    for i in range(len(s)):
        if (s[i] in map_A and map_A[s[i]] != t[i]) or \
            (t[i] in map_B and map_B[t[i]] != s[i]):
            return False
        map_A[s[i]] = t[i]
        map_B[t[i]] = s[i]
    return True

print(isIsomorphic(s1, t1))
print(isIsomorphic(s2, t2))
print(isIsomorphic(s3, t3))
print(isIsomorphic(s4, t4))
            
