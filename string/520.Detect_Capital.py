# 520. Detect Capital
# Example 1:

# Input: 
word1 = "USA"
# Output: true
# Example 2:

# Input: 
word2 = "FlaG"
# Output: false
word3 = "FFFFFFFFFFFFFFFFFFFFf"
#output : false
word4 ="Leetcode"
# Output: true
word5 = "g"
#True

def detectCapitalUse(word: str) -> bool:
    upper = lower = 0 
    for s in word:
        if s.isupper():
            upper += 1
        else:
            lower += 1
    return len(word) == upper or len(word) == lower or (upper == 1 and word[0].isupper())

print(detectCapitalUse(word1))
print(detectCapitalUse(word2))
print(detectCapitalUse(word3))
print(detectCapitalUse(word4))
print(detectCapitalUse(word5))

def detectCapitalUse(word: str) -> bool:
    upper = lower = 0 
    for s in word:
        if s.isupper():
            upper += 1
        else:
            lower += 1
    return len(word) == upper or len(word) == lower or (upper == 1 and word[0].isupper())

print(detectCapitalUse(word1))
print(detectCapitalUse(word2))
print(detectCapitalUse(word3))
print(detectCapitalUse(word4))
print(detectCapitalUse(word5))
