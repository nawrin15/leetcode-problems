# Example 1:

# Input: 
s1 = "loveleetcode"
c1 = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
# Example 2:

# Input: 
s2 = "aaab"
c2 = "b"
# Output: [3,2,1,0]

def shortestToChar(s: str, c: str):
    place = []
    n = len(s)
    res = []
    for i in range(n):
        if s[i] == c:
            place.append(i)
    for i in range(n):
        mini = 100000
        for j in range(len(place)):
            mini = min(mini, abs(i-place[j]))
        res.append(mini)
    return res

print(shortestToChar(s1, c1))
print(shortestToChar(s2, c2))

def shortestToChar1(s: str, c: str):
    n = len(s)
    left = [float('inf')] * n
    right = [float('inf')] * n
    index = -1
    for i in range(n):
        if s[i] == c:
            index = i
            left[i] = 0
        elif index != -1:
            left[i] = abs(i - index)            
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            index = i
            right[i] = 0
        elif index != -1:
            right[i] = abs(i - index)
    return [min(left[i], right[i]) for i in range(n)]
    
print(shortestToChar1(s1, c1))
print(shortestToChar1(s2, c2))