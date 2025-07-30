# Example 1:

# Input: 
n1 = 4
k1 = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:

# Input: 
n2 = 1
k2 = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
 
def combine(n: int, k: int):
    res = []
    def dfs(num, stack):
        if len(stack) == k:
            res.append(stack[:])
            return
        for i in range(num, n + 1):
            stack.append(i)
            dfs(i + 1, stack)
            stack.pop()

    dfs(1, [])
    return res
    

print(combine(n1, k1))
print(combine(n2, k2))