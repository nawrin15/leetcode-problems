# Example 1:

# Input: 
s1 = "(1+(2*3)+((8)/4))+1"

# Output: 3

# Explanation:

# Digit 8 is inside of 3 nested parentheses in the string.

# Example 2:

# Input: 
s2 = "(1)+((2))+(((3)))"

# Output: 3

# Explanation:

# Digit 3 is inside of 3 nested parentheses in the string.

# Example 3:

# Input: 
s3 = "()(())((()()))"

# Output: 3

def maxDepth(s: str) -> int:
    parenthesis = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    stack = []
    maxi = 0
    for i in s:
        if i in parenthesis:
            stack.append(parenthesis[i])
            if maxi < len(stack):
                maxi = len(stack)
        else:
            if i in ")}]":
                stack.pop()
    return maxi


print(maxDepth(s1))
print(maxDepth(s2))
print(maxDepth(s3))

def maxDepth2(s: str) -> int:
    maxi = stack = 0
    for i in s:
        if i == "(":
            stack += 1
            if maxi < stack:
                maxi = stack
        elif i in ")":
                stack -= 1
    return maxi

print(maxDepth2(s1))
print(maxDepth2(s2))
print(maxDepth2(s3))


