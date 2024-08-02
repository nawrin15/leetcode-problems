# Example 1:

# Input: 
s1 = "leetcode"
# Output: 2
# Explanation: The substring "ee" is of length 2 with the character 'e' only.
# Example 2:

# Input: 
s2 = "abbcccddddeeeeedcba"
# Output: 5
# Explanation: The substring "eeeee" is of length 5 with the character 'e' only.


def maxPower(s: str) -> int:
    maxi = 0
    curr_count = 0
    prev_char = s[0]
    for char in s:
        if char == prev_char:
            curr_count += 1
        else:
            curr_count = 1
            prev_char  = char
        if maxi < curr_count:
                maxi = curr_count
    return maxi

print(maxPower(s1))
print(maxPower(s2))
