# Example 1:

# Input: 
s1 = "abaccb"
distance1 = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: true
# Explanation:
# - 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
# - 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
# - 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
# Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
# Return true because s is a well-spaced string.
# Example 2:

# Input: 
s2 = "aa"
distance2 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Output: false
# Explanation:
# - 'a' appears at indices 0 and 1 so there are zero letters between them.
# Because distance[0] = 1, s is not a well-spaced string.
s3 = "abbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzza"
distance3 = [49,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#output: False

def checkDistances(s: str, distance) -> bool:
    d = {}
    for i in range(len(s)):
        if s[i] not in d:
            d[s[i]] = i
        else:
            if i - d[s[i]] - 1 != distance[ord(s[i])-97]:
                return False
    return True

print(checkDistances(s1, distance1))
print(checkDistances(s2, distance2))
print(checkDistances(s3, distance3))