0# Example 1:

# Input: 
word1 = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
# Example 2:

# Input: 
word2 = "aazz"
# Output: false
# Explanation: We must delete a character, so either the frequency of "a" is 1 and 
# the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
word3 = "aaa"
from collections import Counter

def equalFrequency(word: str) -> bool:
    for i in word:
        word_count =  Counter(word)
        word_count[i] -= 1
        if word_count[i] == 0:
            del word_count[i]
        if len(set(word_count.values())) == 1:
            return True
    return False


print(equalFrequency(word1))
print(equalFrequency(word2))
print(equalFrequency(word3))