

def construct2DArray(original, m, n):
    arr = []
    if len(original) == m*n:
        for i in range(0, len(original), n):
            arr.append(original[i:i+n])
    return arr

        
    
original = [1,2,3,4]
m = 2
n = 2

# original = [1,2,3]
# m = 1 
# n = 3

# original = [1,2]
# m = 1 
# n = 1

print(construct2DArray(original, m, n))