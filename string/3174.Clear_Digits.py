# Example 1:

# Input: 
s1 = "abc"

# Output: "abc"

# Explanation:

# There is no digit in the string.

# Example 2:

# Input: 
s2 = "cb34"

# Output: ""

# Explanation:

# First, we apply the operation on s[2], and s becomes "c4".

# Then we apply the operation on s[1], and s becomes "".

def clearDigits(s: str) -> str:
    res = []
    for i in range(len(s)):
        if str.isdigit(s[i]):
            res.pop()
        else:
            res.append(s[i])
    return "".join(res)

print(clearDigits(s1))
print(clearDigits(s2))

def clearDigits(s: str) -> str:
    res = []
    for i in s:
        if str.isdigit(i):
            res.pop()
        else:
            res.append(i)
    return "".join(res)

print(clearDigits(s1))
print(clearDigits(s2))