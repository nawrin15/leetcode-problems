# Example 1:

# Input: 
s1 = "abcdefg" 
k1 = 2
# Output: "bacdfeg"
# Example 2:

# Input: 
s2 = "abcd"
k2 = 2
# Output: "bacd"

def reverseStr(s: str, k: int) -> str:
    res = ''
    for i in range(0, len(s), k*2):
        res += s[i:i+k][::-1]
        res += s[i+k:i+2*k]
    return res

print(reverseStr(s1, k1))
print(reverseStr(s2, k2))