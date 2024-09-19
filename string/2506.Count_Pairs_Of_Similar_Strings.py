# Example 1:

# Input: 
words1 = ["aba","aabb","abcd","bac","aabc"]
# Output: 2
# Explanation: There are 2 pairs that satisfy the conditions:
# - i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
# - i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 
# Example 2:

# Input: 
words2 = ["aabb","ab","ba"]
# Output: 3
# Explanation: There are 3 pairs that satisfy the conditions:
# - i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
# - i = 0 and j = 2 : both words[0] and words[2] only consist of characters 'a' and 'b'.
# - i = 1 and j = 2 : both words[1] and words[2] only consist of characters 'a' and 'b'.
# Example 3:

# Input: 
words3 = ["nba","cba","dba"]
# Output: 0
# Explanation: Since there does not exist any pair that satisfies the conditions, we return 0.

def similarPairs(words) -> int:
    count = 0
    for i in range(len(words)):
        for j in range( i + 1, len(words)):
            if set(words[i]) == set(words[j]):
                count += 1
    return count

print(similarPairs(words1))
print(similarPairs(words2))
print(similarPairs(words3))

def similarPairs1(words) -> int:
    for i in range(len(words)):
        words[i]="".join(sorted(set(words[i])))
    c=0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i]==words[j]:
                c+=1
    return c

print(similarPairs1(words1))
print(similarPairs1(words2))
print(similarPairs1(words3))

from collections import defaultdict
def similarPairs2(words) -> int:
    freq = defaultdict(int)
    for word in words:
        freq[tuple(sorted(set(word)))] += 1
    return sum(value*(value-1)//2  for key, value in freq.items() if value > 1)
         

print(similarPairs2(words1))
print(similarPairs2(words2))
print(similarPairs2(words3))


def similarPairs3(words) -> int:
    aux_dict = defaultdict(int)
    for i in range(len(words)):
        key = "".join(sorted(set(words[i])))
        aux_dict[key] += 1
    res = 0
    for _, count in aux_dict.items():
        if count > 1:
            res += count * (count - 1) // 2
    return res
         

print(similarPairs3(words1))
print(similarPairs3(words2))
print(similarPairs3(words3))