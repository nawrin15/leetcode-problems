# Example 1:


# Input: 
m1 = 2
n1 = 3
indices1 = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.
# Example 2:


# Input: 
m2 = 2
n2 = 2
indices2 = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.

def oddCells(m: int, n: int, indices) -> int:
    res = [[0] * n for _ in range(m)]
    for i in range(len(indices)):
        point = indices[i][0]
        for k in range(n):
            res[point][k] += 1
        point = indices[i][1]
        for k in range(m):
            res[k][point] += 1
    count = 0
    for i in range(m):
        for j in range(n):
            if res[i][j] % 2 == 1:
                count += 1
    return count

print(oddCells(m1, n1, indices1))
print(oddCells(m2, n2, indices2))

def oddCells1(m: int, n: int, indices) -> int:
        rows = [0] * m
        cols = [0] * n
        
        for r, c in indices:
            rows[r] ^= 1
            cols[c] ^= 1
        
        odd_rows = sum(rows)
        odd_cols = sum(cols)
        
        return odd_rows * n + odd_cols * m - 2 * odd_rows * odd_cols

print(oddCells1(m1, n1, indices1))
print(oddCells1(m2, n2, indices2))

def oddCells2(m: int, n: int, indices) -> int:
        row_count = [0] * m
        col_count = [0] * n
        
        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1
        
        odd_rows = sum(1 for x in row_count if x % 2 == 1)
        odd_cols = sum(1 for x in col_count if x % 2 == 1)
        
        even_rows = m - odd_rows
        even_cols = n - odd_cols
        
        return odd_rows * even_cols + odd_cols * even_rows

print(oddCells2(m1, n1, indices1))
print(oddCells2(m2, n2, indices2))

