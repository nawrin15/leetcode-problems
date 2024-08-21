# Example 1:

# Input: 
words1 = ["are","amy","u"]
left1 = 0
right1 = 2
# Output: 2
# Explanation: 
# - "are" is a vowel string because it starts with 'a' and ends with 'e'.
# - "amy" is not a vowel string because it does not end with a vowel.
# - "u" is a vowel string because it starts with 'u' and ends with 'u'.
# The number of vowel strings in the mentioned range is 2.
# Example 2:

# Input: 
words2 = ["hey","aeo","mu","ooo","artro"]
left2 = 1
right2 = 4
# Output: 3
# Explanation: 
# - "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
# - "mu" is not a vowel string because it does not start with a vowel.
# - "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
# - "artro" is a vowel string because it starts with 'a' and ends with 'o'.
# The number of vowel strings in the mentioned range is 3.

def vowelStrings(words, left: int, right: int) -> int:
    count = 0
    for i in range(left, right + 1):
        word = words[i]
        n = len(word)
        if word[0] in 'aeiou' and word[n - 1] in 'aeiou':
            count += 1
    return count

print(vowelStrings(words1, left1, right1))
print(vowelStrings(words2, left2, right2))


def vowelStrings1(words, left: int, right: int) -> int:
    count = 0
    vowel = 'aeiou'
    for word in words[left:right + 1]:
        if word[0] in vowel and word[-1] in vowel:
            count += 1
    return count

print(vowelStrings1(words1, left1, right1))
print(vowelStrings1(words2, left2, right2))

def vowelStrings2(words, left: int, right: int) -> int:
    vowel = {'a','e','i','o','u'}
    return sum(1 for word in words[left:right + 1] if word[0] in vowel and word[-1] in vowel)

print(vowelStrings2(words1, left1, right1))
print(vowelStrings2(words2, left2, right2))