# Example 1:

# Input: 
s1 = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: 
s2 = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: 
s3 = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


def lengthOfLastWord1(s: str) -> int:
        s = s.strip()
        chunk = s.split(" ")
        n = len(chunk)
        return len(chunk[-1])

def lengthOfLastWord2(s: str) -> int:
        s = s.split()
        s = s[-1]
        return len(s)

def lengthOfLastWord3(s: str) -> int:
    if len(s) == 0:
        return -1
    
    
    counter = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == ' ':
            if counter != 0:
                return counter
        else:
            counter += 1
    return counter


print(lengthOfLastWord1(s1))
print(lengthOfLastWord1(s2))
print(lengthOfLastWord1(s3))


print(lengthOfLastWord2(s1))
print(lengthOfLastWord2(s2))
print(lengthOfLastWord2(s3))


print(lengthOfLastWord3(s1))
print(lengthOfLastWord3(s2))
print(lengthOfLastWord3(s3))