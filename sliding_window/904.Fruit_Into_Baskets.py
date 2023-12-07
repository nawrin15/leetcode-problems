maxFruits = left = 0 
# trees = [1,2,3,2,2]
trees = [1,2,1]
# trees = [1,2,1,1,3,4,2,2,2,2,4]
treeTypesMap = {}

for right in range(len(trees)):
    treeType = trees[right]
    if treeType not in treeTypesMap:
        treeTypesMap[treeType] = 0
    treeTypesMap[treeType] = treeTypesMap[treeType] + 1
    
    while (len(treeTypesMap) > 2):
        fruitCount = treeTypesMap[trees[left]] 
        if fruitCount == 1:
            del treeTypesMap[trees[left]]
        else:
            treeTypesMap[trees[left]] = treeTypesMap[trees[left]] - 1
        left += 1
    maxFruits = max(maxFruits, right - left + 1 )
    
print(maxFruits)
            
