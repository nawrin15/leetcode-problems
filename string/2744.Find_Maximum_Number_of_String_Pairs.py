# Example 1:

# Input: 
words1 = ["cd","ac","dc","ca","zz"]
# Output: 2
# Explanation: In this example, we can form 2 pair of strings in the following way:
# - We pair the 0th string with the 2nd string, as the reversed string of word[0] is "dc" and is equal to words[2].
# - We pair the 1st string with the 3rd string, as the reversed string of word[1] is "ca" and is equal to words[3].
# It can be proven that 2 is the maximum number of pairs that can be formed.
# Example 2:

# Input: 
words2 = ["ab","ba","cc"]
# Output: 1
# Explanation: In this example, we can form 1 pair of strings in the following way:
# - We pair the 0th string with the 1st string, as the reversed string of words[1] is "ab" and is equal to words[0].
# It can be proven that 1 is the maximum number of pairs that can be formed.
# Example 3:

# Input:
words3 = ["aa","ab"]
# Output: 0
# Explanation: In this example, we are unable to form any pair of strings.

def maximumNumberOfStringPairs(words) -> int:
    w = {}
    count = 0
    for word in words:
        if word in w:
            count += 1
        w[word[::-1]] = 1
    return count

print(maximumNumberOfStringPairs(words1))
print(maximumNumberOfStringPairs(words2))
print(maximumNumberOfStringPairs(words3))

def maximumNumberOfStringPairs2(words) -> int:
    count = 0
    for word in words:
        word_rev = word[::-1]
        if word != word_rev and word[::-1] in words:
            count += 1
            words.remove(word_rev)
    return count

print(maximumNumberOfStringPairs2(words1))
print(maximumNumberOfStringPairs2(words2))
print(maximumNumberOfStringPairs2(words3))