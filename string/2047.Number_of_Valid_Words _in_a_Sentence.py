# Example 1:

# Input: 
sentence1 = "cat and  dog"
# Output: 3
# Explanation: The valid words in the sentence are "cat", "and", and "dog".
# Example 2:

# Input: 
sentence2 = "!this  1-s b8d!"
# Output: 0
# Explanation: There are no valid words in the sentence.
# "!this" is invalid because it starts with a punctuation mark.
# "1-s" and "b8d" are invalid because they contain digits.
# Example 3:

# Input: 
sentence3 = "alice and  bob are playing stone-game10"
# Output: 5
# Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
# "stone-game10" is invalid because it contains digits.

def countValidWords(sentence: str) -> int:
    words = str.split(sentence)
    print(words)
    return

print(countValidWords(sentence1))
print(countValidWords(sentence2))
