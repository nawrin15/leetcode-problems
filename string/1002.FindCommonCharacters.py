# Example 1:

# Input: 
words1 = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: 
words2 = ["cool","lock","cook"]
# Output: ["c","o"]

def commonChars(words):
    res = set(words[0])
    for i in range(1, len(words)):
        word_set = set(words[i])
        res &= word_set

    return list(res)

print(commonChars(words1))
print(commonChars(words2))