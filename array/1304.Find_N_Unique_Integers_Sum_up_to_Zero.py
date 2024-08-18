# Example 1:

# Input: 
n1 = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:

# Input: 
n2 = 3
# Output: [-1,0,1]
# Example 3:

# Input: 
n3 = 1
# Output: [0]

def sumZero(n: int):
    res = []
    if n % 2 == 1:
        res.append(0)
    for i in range(n//2):
        res.append(i + 1)
        res.append(-(i + 1))
    return res

print(sumZero(n1))
print(sumZero(n2))
print(sumZero(n3))


def sumZero1(n: int):
    return [i*2 - n + 1 for i in range(n)]

print(sumZero1(n1))
print(sumZero1(n2))
print(sumZero1(n3))