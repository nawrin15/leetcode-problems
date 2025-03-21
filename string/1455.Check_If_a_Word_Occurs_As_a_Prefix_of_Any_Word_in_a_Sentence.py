# Example 1:

# Input: 
sentence1 = "i love eating burger"
searchWord1 = "burg"
# Output: 4
# Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
# Example 2:

# Input: 
sentence2 = "this problem is an easy problem"
searchWord2 = "pro"
# Output: 2
# Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence, but we return 2 as it's the minimal index.
# Example 3:

# Input: 
sentence3 = "i am tired"
searchWord3 = "you"
# Output: -1
# Explanation: "you" is not a prefix of any word in the sentence.

def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    count = 0
    for word in sentence.split(" "):
        count += 1
        if searchWord==word[:len(searchWord)]:
            return count
    return -1


print(isPrefixOfWord(sentence1, searchWord1))
print(isPrefixOfWord(sentence2, searchWord2))
print(isPrefixOfWord(sentence3, searchWord3))


def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    for index, word in enumerate(sentence.split(" ")):
        if word.startswith(searchWord):
            return index + 1
    return -1


print(isPrefixOfWord(sentence1, searchWord1))
print(isPrefixOfWord(sentence2, searchWord2))
print(isPrefixOfWord(sentence3, searchWord3))