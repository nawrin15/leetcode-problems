# Example 1:

# Input: 
s1 = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
# Example 2:

# Input: 
s2 = "Hello"
# Output: 1
s3=", , , ,        a, eaefa"
# output 6
s4="Of all the gin joints in all the towns in all the world,   "
#output: 13
s5="                "
#output: 0
s6=""
#output: 0

def countSegments(s: str) -> int:
    return sum(1 if s[i] != ' ' and (i == 0 or s[i - 1] == ' ') else 0 for i in range(len(s)))

print(countSegments(s1))
print(countSegments(s2))
print(countSegments(s3))
print(countSegments(s4))
print(countSegments(s5))
print(countSegments(s6))

def countSegments(s: str) -> int:
    return len(s.split())

print(countSegments(s1))
print(countSegments(s2))
print(countSegments(s3))
print(countSegments(s4))
print(countSegments(s5))
print(countSegments(s6))

def countSegments(s: str) -> int:
    s = s.split(' ')
    count = 0 
    for word in s:
        if len(word.split()) > 0:
            count += 1
    return count

print(countSegments(s1))
print(countSegments(s2))
print(countSegments(s3))
print(countSegments(s4))
print(countSegments(s5))
print(countSegments(s6))