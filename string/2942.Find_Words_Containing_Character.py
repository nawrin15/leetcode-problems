# Example 1:

# Input: 
words1 = ["leet","code"]
x1 = "e"
# Output: [0,1]
# Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
# Example 2:

# Input: 
words2 = ["abc","bcd","aaaa","cbc"]
x2 = "a"
# Output: [0,2]
# Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
# Example 3:

# Input: 
words3 = ["abc","bcd","aaaa","cbc"]
x3 = "z"
# Output: []
# Explanation: "z" does not occur in any of the words. Hence, we return an empty array.
 
def findWordsContaining(words, x: str):
    res = []
    for i in range(len(words)):
        if x in words[i]:
            res.append(i)
    return res

print(findWordsContaining(words1, x1))
print(findWordsContaining(words2, x2))
print(findWordsContaining(words3, x3))