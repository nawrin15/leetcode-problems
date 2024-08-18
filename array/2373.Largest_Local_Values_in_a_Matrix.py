# Example 1:
# Input: 
grid1 = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
# Output: [[9,9],[8,6]]
# Explanation: The diagram above shows the original matrix and the generated matrix.
# Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
# Example 2:


# Input: 
grid2 = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
# Output: [[2,2,2],[2,2,2],[2,2,2]]
# Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.

def findMaxLocal(row, col, grid):
    maxi = -1
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            maxi = max(maxi, grid[i][j])
    return maxi

def largestLocal(grid):
    n = len(grid)
    maxLocal = [[0]*(n-2) for _ in range(n-2)]
    for i in range(n-2):
        for j in range(n-2):
            maxLocal[i][j] = findMaxLocal(i, j, grid)
    return maxLocal

print(largestLocal(grid1))
print(largestLocal(grid2))



def largestLocal(grid):
    n = len(grid)
    maxLocal = [[0]*(n-2) for _ in range(n-2)]
    for row in range(n-2):
        for col in range(n-2):
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    maxLocal[row][col] = max(maxLocal[row][col], grid[i][j])
    return maxLocal

print(largestLocal(grid1))
print(largestLocal(grid2))

