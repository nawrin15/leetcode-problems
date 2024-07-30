# Example 1:

# Input: 
s1 = "hello"

# Output: 13

# Explanation:

# The ASCII values of the characters in s are: 
# 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. 
# So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:

# Input: 
s2 = "zaz"

# Output: 50

# Explanation:

# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s 
# would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

def scoreOfString(s: str) -> int:
    return sum(abs(ord(s[i])-ord(s[i+1])) for i in range(len(s) - 1))

print(scoreOfString(s1))
print(scoreOfString(s2))