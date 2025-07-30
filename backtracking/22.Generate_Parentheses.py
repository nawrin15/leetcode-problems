# Example 1:

# Input: 
n1 = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: 
n2 = 1
# Output: ["()"]
 


def generateParenthesis(n: int):
    res = []
    stack = []
    def dfs(open, close, stack):
        if len(stack) == n * 2:
            res.append("".join(stack))
            return
        if open < n:
            stack.append('(')
            dfs(open + 1, close, stack)
            stack.pop()
        if close < open:
            stack.append(')')
            dfs(open, close + 1, stack)
            stack.pop()
    dfs(0, 0, stack)
    return res

print(generateParenthesis(n1))
print(generateParenthesis(n2))