# Example 1:

# Input: 
grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.
# Example 2:

# Input: 
grid2 = [[3,2],[1,0]]
# Output: 0

def countNegatives(grid) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] < 0:
                count += 1
    return count

print(countNegatives(grid1))
print(countNegatives(grid2))

def countNegatives1(grid) -> int:
    count = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if grid[i][mid] < 0:
                right = mid
            else:
                left = mid + 1
        count += n - left
    return count

print(countNegatives1(grid1))
print(countNegatives1(grid2))