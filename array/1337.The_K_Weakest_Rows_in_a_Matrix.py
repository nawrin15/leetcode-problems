# Example 1:

# Input: 
mat1 = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k1 = 3
# Output: [2,0,3]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 2 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 2 
# - Row 4: 5 
# The rows ordered from weakest to strongest are [2,0,3,1,4].
# Example 2:

# Input: 
mat2 = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]] 
k2 = 2
# Output: [0,2]
# Explanation: 
# The number of soldiers in each row is: 
# - Row 0: 1 
# - Row 1: 4 
# - Row 2: 1 
# - Row 3: 1 
# The rows ordered from weakest to strongest are [0,2,3,1].


def kWeakestRows(mat, k: int):
    n = len(mat)
    freq = [0] * n
    for i in range(n):
        freq[i] += mat[i].count(1)
    res = []
    mini = 1000
    index = -1
    while k != 0:
       index = -1
       mini = 1000
       for i in range(n):
           if freq[i] < mini:
               mini = freq[i]
               index = i
       res.append(index)
       freq[index] = 1000
       k -= 1
    return res

print(kWeakestRows(mat1, k1))
print(kWeakestRows(mat2, k2))


def kWeakestRows1(mat, k: int):
    freq = {}
    for i in range(0,len(mat)):
        solders = mat[i].count(1)
        freq[i] = solders
    ans = sorted(freq.keys(), key = lambda x:freq[x])
    
    return ans[:k]

print(kWeakestRows1(mat1, k1))
print(kWeakestRows1(mat2, k2))


