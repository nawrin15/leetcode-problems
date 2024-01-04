grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [["1","1","1"],["0","1","0"],["1","1","1"]]


# if not grid:
#   return 0

def dfs(grid, i, j):
  
  if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
    return
  
  grid[i][j] = '2'
  dfs(grid, i + 1, j)
  dfs(grid, i - 1, j)
  dfs(grid, i, j + 1)
  dfs(grid, i, j - 1)
  
num_of_island = 0
for i in range(len(grid)):
  for j in range(len(grid[0])):
    if grid[i][j] == '1':
      dfs(grid, i, j)
      num_of_island += 1
      
print(num_of_island)
      

    