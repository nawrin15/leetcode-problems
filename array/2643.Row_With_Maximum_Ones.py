# Example 1:

# Input: 
mat1 = [[0,1],[1,0]]
# Output: [0,1]
# Explanation: Both rows have the same number of 1's. So we return the index of the smaller row, 0, and the maximum count of ones (1). So, the answer is [0,1]. 
# Example 2:

# Input: 
mat2 = [[0,0,0],[0,1,1]]
# Output: [1,2]
# Explanation: The row indexed 1 has the maximum count of ones (2). So we return its index, 1, and the count. So, the answer is [1,2].
# Example 3:

# Input: 
mat3 = [[0,0],[1,1],[0,0]]
# Output: [1,2]
# Explanation: The row indexed 1 has the maximum count of ones (2). 
# So the answer is [1,2].def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
mat4 = [[0,1],[1,1]]


def rowAndMaximumOnes(mat): 
    m, n = len(mat), len(mat[0])
    res = [0] * m
    max_num = 0
    for i in range(m):
        for j in range(n):
            res[i] += mat[i][j]
        if res[i] > max_num:
            max_num = res[i]
    for i in range(m):
        if res[i] == max_num:
            return [i, res[i]]
    return [0, 0]

        

print(rowAndMaximumOnes(mat1))
print(rowAndMaximumOnes(mat2))
print(rowAndMaximumOnes(mat3))
print(rowAndMaximumOnes(mat4))

def rowAndMaximumOnes1(mat): 
    max_num = 0
    index = 0
    for i in range(len(mat)):
        curr_counter = mat[i].count(1)
        if curr_counter > max_num:
            max_num = curr_counter
            index = i
    return [index, max_num]

        

print(rowAndMaximumOnes1(mat1))
print(rowAndMaximumOnes1(mat2))
print(rowAndMaximumOnes1(mat3))
print(rowAndMaximumOnes1(mat4))

def rowAndMaximumOnes2(mat): 
    count = [i.count(1) for i in mat]
    return [count.index(max(count)),max(count)]

        

print(rowAndMaximumOnes2(mat1))
print(rowAndMaximumOnes2(mat2))
print(rowAndMaximumOnes2(mat3))
print(rowAndMaximumOnes2(mat4))