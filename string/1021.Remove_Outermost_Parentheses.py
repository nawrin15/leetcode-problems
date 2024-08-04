# Example 1:

# Input: 
s1 = "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: 
s2 = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: 
s3 = "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".

def removeOuterParentheses(s: str) -> str:
    stack = 0
    res = ""
    for i in s:
        if i == "(" and stack > 0:
            res += i
        elif i == ")" and stack > 1:
            res += i 
        stack += 1 if i == "(" else -1       
    return res

print(removeOuterParentheses(s1))
print(removeOuterParentheses(s2))
print(removeOuterParentheses(s3))