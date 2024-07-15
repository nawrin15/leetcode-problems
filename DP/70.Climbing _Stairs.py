# Example 1:

# Input: 
n1 = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: 
n2 = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Bottomup dynamc programing
def climbStairs(n: int) -> int:
    one, two = 1, 1
    for i in range(n - 1):
        temp = one
        one = one + two
        two = temp
    return one

def climbStairs1(n: int) -> int:
    if n == 1: return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2 
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(climbStairs(n1))
print(climbStairs(n2))

print(climbStairs1(n1))
print(climbStairs1(n2))