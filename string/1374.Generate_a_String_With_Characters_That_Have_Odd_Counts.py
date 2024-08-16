# Example 1:

# Input: 
n1 = 4
# Output: "pppz"
# Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".
# Example 2:

# Input: 
n2 = 2
# Output: "xy"
# Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".
# Example 3:

# Input: 
n3 = 7
# Output: "holasss"
n4 = 1

def generateTheString(n: int) -> str:
    if n == 1:
        return 'a'
    elif n % 2 == 0:
        return 'a' * (n-1) + 'b' * 1
    else:
        return 'a' * (n-2) + 'bc'

print(generateTheString(n1))
print(generateTheString(n2))
print(generateTheString(n3))
print(generateTheString(n4))

def generateTheString1(n: int) -> str:
    return 'a' * n if n % 2 == 1 else 'a' * (n-1) + 'b' 
        
print(generateTheString1(n1))
print(generateTheString1(n2))
print(generateTheString1(n3))
print(generateTheString1(n4))