# Solution - 1
maxFruits = left = 0 
# trees = [1,2,3,2,2]
trees = [1,2,1]
trees = [1,2,1,1,3,4,2,2,2,2,4]
treeTypesMap = {}

for right in range(len(trees)):
    treeType = trees[right]
    # if treeType not in treeTypesMap:
    #     treeTypesMap[treeType] = 0
    # treeTypesMap[treeType] = treeTypesMap[treeType] + 1
    treeTypesMap[treeType] = treeTypesMap.get(treeType, 0) + 1
    
    while (len(treeTypesMap) > 2):
        fruitCount = treeTypesMap[trees[left]] 
        if fruitCount == 1:
            del treeTypesMap[trees[left]]
        else:
            treeTypesMap[trees[left]] = treeTypesMap[trees[left]] - 1
        left += 1
    maxFruits = max(maxFruits, right - left + 1 )
    
print(maxFruits)
         
# Solution - 2   
maxFruits = start = 0 
trees = [1,2,3,2,2]
trees = [1,2,1]
trees = [1,2,1,1,3,4,2,2,2,2,4]
treeTypesMap = {}

for end in range(len(trees)):
    treeType = trees[end]
    if len(treeTypesMap) < 2 and (treeType not in treeTypesMap):
        treeTypesMap[treeType] = True
        maxFruits = max(maxFruits, end - start + 1)
    elif treeType in treeTypesMap:
        maxFruits = max(maxFruits, end - start + 1)
    else:
        treeTypesMap = {}
        treeTypesMap[trees[end-1]] = True
        treeTypesMap[treeType] = True
        start = end - 1
        
        while trees[start] == trees[start - 1]:
            start -= 1
        maxFruits = max(maxFruits, end - start + 1)

print(maxFruits)

# Solution - 2   
count, i = {}, 0
for j, v in enumerate(trees):
    count[v] = count.get(v, 0) + 1
    if len(count) > 2:
        count[trees[i]] -= 1
        if count[trees[i]] == 0: del count[trees[i]]
        i += 1
print(j - i + 1)