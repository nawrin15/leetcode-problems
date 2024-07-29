# Example 1:

# Input: 
names1 = ["Mary","John","Emma"]
heights1 = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:

# Input: 
names2 = ["Alice","Bob","Bob"]
heights2 = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

def sortPeople(names, heights):
    n = len(heights)
    for i in range(n):
        for j in range(i+1, n):
            if heights[i] < heights[j]:
                temp = heights[i]
                heights[i] = heights[j]
                heights[j] = temp
                temp = names[i]
                names[i] = names[j]
                names[j] = temp
    return names

def sortPeople1(names, heights):
    res = []
    for i in range(len(names)):
        res.append([heights[i],names[i]])
    res = sorted(res,reverse=True)
    return [name for height,name in res]


def sortPeople2(names, heights):
    height_dict = dict(zip(heights,names)) # // height_dict = {180: 'Mary', 165: 'John', 170: 'Emma'}
    names.clear()
    for key in sorted(height_dict.keys(),reverse=True):
        names.append(height_dict[key])
    return names
                
print(sortPeople(names1, heights1))
print(sortPeople(names2, heights2))

print(sortPeople1(names1, heights1))
print(sortPeople1(names2, heights2))

print(sortPeople2(names1, heights1))
print(sortPeople2(names2, heights2))
