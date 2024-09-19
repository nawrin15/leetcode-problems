# Example 1:

# Input: 
s1 = "IDID"
# Output: [0,4,1,3,2]
# Example 2:

# Input: 
s2 = "III"
# Output: [0,1,2,3]
# Example 3:

# Input: 
s3 = "DDI"
# Output: [3,2,0,1]

def diStringMatch(s: str):
    res = []
    i, j = 0, len(s)
    for k in s:
        if k == "I":
            res.append(i)
            i += 1
        else:
            res.append(j)
            j -= 1
    res.append(i)
    return res

print(diStringMatch(s1))
print(diStringMatch(s2))
print(diStringMatch(s3))