# A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), 
# hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. 
# Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

# A token is a valid word if all three of the following are true:

# It only contains lowercase letters, hyphens, and/or punctuation (no digits).
# There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters 
# ("a-b" is valid, but "-ab" and "ab-" are not valid).
# There is at most one punctuation mark. If present, it must be at the end of the 
# token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
# Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

# Given a string sentence, return the number of valid words in sentence.


# Example 1:

# Input: 
sentence1 = "cat and  dog"
# Output: 3
# Explanation: The valid words in the sentence are "cat", "and", and "dog".
# Example 2:

# Input: 
sentence2 = "!thiS  1-s b8d!"
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

import re 

def countValidWords(sentence: str) -> int:
    pattern = re.compile('(^[a-z]+(-[a-z]+)?)?[,.!]?$')
    return sum(bool(pattern.match(word)) for word in sentence.split())

print(countValidWords(sentence1))
print(countValidWords(sentence2))

def countValidWords1(sentence: str) -> int:
    count = 0
    for word in sentence.split():
        if bool(re.search('\d', word)):
            continue
        if bool(re.search('^[a-z][.,!][-]', word)):
            continue
        print(word)
    return count

print(countValidWords1(sentence1))
print(countValidWords1(sentence2))