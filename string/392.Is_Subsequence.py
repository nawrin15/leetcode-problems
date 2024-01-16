
s = "abc"
t = "ahbgdc"

def isSubsequence(s: str, t: str) -> bool:     
    if len(s) == 0:
        return True
    if len(s) > len(t):
        return False

    cur = 0
    for i in range(len(t)):
        if s[cur] == t[i]:
            cur += 1
        if cur == len(s):
            return True
            
            
    return False

print("isSubsequence:", isSubsequence(s, t))