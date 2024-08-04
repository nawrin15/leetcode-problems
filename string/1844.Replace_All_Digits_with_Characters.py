# Example 1:

# Input: 
s1 = "a1c1e1"
# Output: "abcdef"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('c',1) = 'd'
# - s[5] -> shift('e',1) = 'f'
# Example 2:

# Input: 
s2 = "a1b2c3d4e"
# Output: "abbdcfdhe"
# Explanation: The digits are replaced as follows:
# - s[1] -> shift('a',1) = 'b'
# - s[3] -> shift('b',2) = 'd'
# - s[5] -> shift('c',3) = 'f'
# - s[7] -> shift('d',4) = 'h'Example 1:


def replaceDigits(s: str) -> str:
    res = ""
    for i in range(0,len(s), 2):
        res += s[i] + (chr(ord(s[i]) + int(s[i + 1])) if len(s) > (i + 1) else "") 
    return res

print(replaceDigits(s1))
print(replaceDigits(s2))

def replaceDigits2(s: str) -> str:
    return "".join([s[i] + (chr(ord(s[i]) + int(s[i + 1])) if len(s) > (i + 1) else "") for i in range(0, len(s), 2)])

print(replaceDigits2(s1))
print(replaceDigits2(s2))