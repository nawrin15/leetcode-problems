# Example 1:

# Input: 
word1 = "aaAbcBC"

# Output: 3

# Explanation:

# The special characters in word are 'a', 'b', and 'c'.

# Example 2:

# Input: 
word2 = "abc"

# Output: 0

# Explanation:

# No character in word appears in uppercase.

# Example 3:

# Input: 
word3 = "abBCab"

# Output: 1

# Explanation:

# The only special character in word is 'b'.

def numberOfSpecialChars(word: str) -> int:
    
    return