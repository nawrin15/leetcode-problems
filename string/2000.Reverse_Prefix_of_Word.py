# Example 1:

# Input: 
word1 = "abcdefd"
ch1 = "d"
# Output: "dcbaefd"
# Explanation: The first occurrence of "d" is at index 3. 
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
# Example 2:

# Input: 
word2 = "xyxzxe"
ch2 = "z"
# Output: "zxyxxe"
# Explanation: The first and only occurrence of "z" is at index 3.
# Reverse the part of word from 0 to 3 (inclusive), the resulting string is "zxyxxe".
# Example 3:

# Input: 
word3 = "abcd"
ch3 = "z"
# Output: "abcd"
# Explanation: "z" does not exist in word.
# You should not do any reverse operation, the resulting string is "abcd".
#word1 = "abcdefd"
def reversePrefix(word: str, ch: str) -> str:

    for i in range(len(word)):
        if word[i] == ch:
            return word[i::-1] + word[i + 1:]
    return word

def reversePrefix2(word: str, ch: str) -> str:
        i = word.find(ch)
        s = word[:i + 1]
        temp = ""
        if i + 1 < len(word):
            temp = word[i + 1:]
        s = s[::-1]
        return s + temp  

print(reversePrefix(word1, ch1))
print(reversePrefix(word2, ch2))
print(reversePrefix(word3, ch3))

print(reversePrefix2(word1, ch1))
print(reversePrefix2(word2, ch2))
print(reversePrefix2(word3, ch3))