# Example 1:

# Input: 
s1 = "5F3Z-2e-9-w"
k1 = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
# Example 2:

# Input: 
s2 = "2-5g-3-J"
k2 = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2 characters except 
# the first part as it could be shorter as mentioned above.
 
def licenseKeyFormatting(s: str, k: int):
    res = []
    temp = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "-":
            temp.append(s[i])
        if len(temp) == k:
            res.append("".join(temp[::-1]))
            temp = []
    if len(temp) != 0: 
        res.append("".join(temp[::-1]))
    return "-".join(res[::-1]).upper()

print(licenseKeyFormatting(s1, k1))
print(licenseKeyFormatting(s2, k2))

def licenseKeyFormatting2(s: str, k: int):
    s = s.replace("-", "").upper()
    first_group_size = len(s) % k
    res = []
    if first_group_size:
        res.append(s[:first_group_size])
    
    for i in range(first_group_size, len(s), k):
        res.append(s[i:i+k])
    return "-".join(res)

print(licenseKeyFormatting2(s1, k1))
print(licenseKeyFormatting2(s2, k2))