s1 = "()"
#Output: true

s2 = "()[]{}"
#Output: true

s3 = "(]"
#Output: false

def isValid(s):
    brackets = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
    stack = []
    for char in s:
        if char in brackets:
            stack.append(char)
        elif len(stack) == 0 or brackets[stack.pop()] != char:
            return False
    return not stack 

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
    