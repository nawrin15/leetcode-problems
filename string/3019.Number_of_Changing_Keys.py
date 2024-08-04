# Example 1:

# Input: 
s1 = "aAbBcC"
# Output: 2
# Explanation: 
# From s[0] = 'a' to s[1] = 'A', there is no change of key as caps lock or shift is not counted.
# From s[1] = 'A' to s[2] = 'b', there is a change of key.
# From s[2] = 'b' to s[3] = 'B', there is no change of key as caps lock or shift is not counted.
# From s[3] = 'B' to s[4] = 'c', there is a change of key.
# From s[4] = 'c' to s[5] = 'C', there is no change of key as caps lock or shift is not counted.

# Example 2:

# Input: 
s2 = "AaAaAaaA"
# Output: 0
# Explanation: There is no change of key since only the letters 'a' and 'A' are pressed which does not require change of key.
 
def countKeyChanges(s: str) -> int:
    s = s.lower()
    count = 0
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            count += 1 
    return count

print(countKeyChanges(s1))
print(countKeyChanges(s2))
