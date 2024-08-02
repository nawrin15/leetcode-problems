# Example 1:

# Input: 
allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]
# Output: 2
# Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
# Example 2:

# Input: 
allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]
# Output: 7
# Explanation: All strings are consistent.
# Example 3:

# Input: 
allowed3 = "cad"
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]
# Output: 4
# Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

def countConsistentStrings(allowed: str, words) -> int:
    count = 0
    for word in words:
        flag = 0
        for i in word:
            if i not in allowed:
                flag = 1
                break
        if flag == 0:
            count += 1
    return count

print(countConsistentStrings(allowed1, words1))
print(countConsistentStrings(allowed2, words2))
print(countConsistentStrings(allowed3, words3))


def countConsistentStrings(allowed: str, words) -> int:
    count = 0
    allowed_set = set(allowed)
    for word in words:       
        if len(set(word) - allowed_set) == 0:
            count += 1
    return count

print(countConsistentStrings(allowed1, words1))
print(countConsistentStrings(allowed2, words2))
print(countConsistentStrings(allowed3, words3))

def countConsistentStrings(allowed: str, words) -> int:
    allowedset=set(allowed)
    count=0
    for i in words:
        if set(i).issubset(allowedset):
            count+=1
    return count

print(countConsistentStrings(allowed1, words1))
print(countConsistentStrings(allowed2, words2))
print(countConsistentStrings(allowed3, words3))

def countConsistentStrings(allowed: str, words) -> int:
    s = set(allowed)
    return sum(all(c in s for c in w) for w in words)

print(countConsistentStrings(allowed1, words1))
print(countConsistentStrings(allowed2, words2))
print(countConsistentStrings(allowed3, words3))