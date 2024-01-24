from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p1 = TreeNode(
    val = 10,
    left = TreeNode(
                val = 5, 
                left = TreeNode(
                    val=3, 
                    left=TreeNode(
                        val=3, 
                        left=None,
                        right=None
                    ),
                    right=TreeNode(
                        val=-2, 
                        left=None,
                        right=None
                    )
                ),
                right = TreeNode(
                        val=2, 
                        left=None,
                        right=TreeNode(
                            val=1, 
                            left=None,
                            right=None
                        )
                    )
        ),
    right = TreeNode(
                val=-3, 
                left= None, 
                right=TreeNode(
                    val=11, 
                    left=None,
                    right=None
                )
            )
    
)

p2 = TreeNode(
    val = 5,
    left = TreeNode(
                val = 4, 
                left = TreeNode(
                    val=11, 
                    left=TreeNode(
                        val=7, 
                        left=None,
                        right=None
                    ),
                    right=TreeNode(
                        val=2, 
                        left=None,
                        right=None
                    )
                ),
                right = None
        ),
    right = TreeNode(
                val=8, 
                left= TreeNode(
                    val=13, 
                    left=None,
                    right=None
                ), 
                right=TreeNode(
                    val=4, 
                    left=TreeNode(
                        val=5, 
                        left=None,
                        right=None
                    ),
                    right=TreeNode(
                        val=1, 
                        left=None,
                        right=None
                    )
                )
            )
    
)

p3 = TreeNode(
    val = 1,
    left = None,
    right = TreeNode(
                val = 2, 
                left = None,
                right = TreeNode(
                    val = 3, 
                    left= None,
                    right=TreeNode(
                        val=4, 
                        left=None,
                        right=TreeNode(
                            val=5, 
                            left=None,
                            right=None
                        )
                    )
                )
            )
    
)

def path_sum_III_1(root, targetSum) -> bool:
    
    
    def dfs(root, sum):
        if not root: return 0
        count = 0 
        sum += root.val
        if sum == targetSum:
           count += 1 
        count += dfs(root.left, sum)
        count += dfs(root.right, sum)
        return count
    
    
    if not root: return 0
    return path_sum_III_1(root.left, targetSum) + dfs(root, 0) + path_sum_III_1(root.right, targetSum)
        

##Solution-2 (with using extra variable to store sum)
def path_sum_III_2(root, targetSum) -> bool:
        
    def dfs(root, targetSum):
        if not root: return 0
        
        count = 0
        targetSum -= root.val
        if targetSum == 0:
            count += 1
        count += dfs(root.left, targetSum)
        count += dfs(root.right, targetSum)
        return count
    
    if not root: return 0
    return dfs(root, targetSum) + path_sum_III_2(root.right, targetSum) + path_sum_III_2(root.left, targetSum)

##Solution-3 (with using map)
class Solution:
    def path_sum_III_3(self, root, targetSum) -> bool:
        
        self.sum_map = defaultdict(int)
        self.count = 0
        
        
        def dfs(root, currentSum):
            if not root: return 
            
            currentSum += root.val
            self.count += self.sum_map[currentSum]
            self.sum_map[currentSum + targetSum] += 1
            dfs(root.left, currentSum)
            dfs(root.right, currentSum)
            self.sum_map[currentSum + targetSum] -= 1
        
        if not root: return 0
        self.sum_map[targetSum] = 1
        dfs(root, 0)
        return self.count

##Solution-4 (with using map)
class Solutionk:
    def path_sum_III_4(self, root, targetSum) -> bool:
        
        self.sum_map = defaultdict(int)
        self.count = 0
        
        
        def dfs(root, currentSum):
            if not root: return 
            
            currentSum += root.val
            self.count += self.sum_map[currentSum]
            self.sum_map[currentSum + targetSum] += 1
            dfs(root.left, currentSum)
            dfs(root.right, currentSum)
            self.sum_map[currentSum + targetSum] -= 1
        
        if not root: return 0
        self.sum_map[targetSum] = 1
        dfs(root, 0)
        return self.count
    
##Solution-5 (with using map)
class Solutionm:
    def path_sum_III_5(self, root, targetSum) -> bool:
        
        self.sum_map = {0:1}
        self.count = 0
        
        
        def dfs(root, currentSum):
            if not root: return 
            print("visiting node val = ", root.val)
            print(self.sum_map)
            
            currentSum += root.val
            if (currentSum - targetSum) in self.sum_map:
                self.count += self.sum_map[currentSum - targetSum]
                
            self.sum_map[currentSum] = self.sum_map.get(currentSum, 0) + 1
            
            dfs(root.left, currentSum)
            dfs(root.right, currentSum)
            self.sum_map[currentSum] -= 1
        
        dfs(root, 0)
        return self.count

##Solution-6 (with using map)
class Solutionn:
    def path_sum_III_6(self, root, targetSum) -> bool:
        
        self.sum_map = {}
        self.count = 0
        
        
        def dfs(root, currentSum):
            if not root: return 
            print("visiting node val = ", root.val)
            print(self.sum_map)
            
            currentSum += root.val
            if currentSum == targetSum: 
                self.count += 1
            if (currentSum - targetSum) in self.sum_map:
                self.count += self.sum_map[currentSum - targetSum]
            
            print("count", self.count)
                
            self.sum_map[currentSum] = self.sum_map.get(currentSum, 0) + 1
            
            dfs(root.left, currentSum)
            dfs(root.right, currentSum)
            # backtrack
            self.sum_map[currentSum] -= 1
        
        dfs(root, 0)
        return self.count
    
##Solution-7 (with using map)
class Solutiono:
    def path_sum_III_7(self, root, targetSum) -> bool:
        
        self.count = 0
        
        def dfs(root, currList):
            if not root: return 
            print("visiting node val = ", root.val)
            print(currList)
            
            currList.append(root.val)
            currentSum = 0
            for i in range(len(currList)-1, -1, -1):
                currentSum += currList[i]
                if currentSum == targetSum: 
                    self.count += 1
             
            print("count", self.count)
                            
            dfs(root.left, currList)
            dfs(root.right, currList)
            # backtrack
            currList.pop()
        
        dfs(root, [])
        return self.count
    
    
print("path sum equal: ", path_sum_III_1(p1, 8))
print("path sum equal: ", path_sum_III_1(p2, 22))
print("path sum equal: ", path_sum_III_1(p3, 3))
print("\n")
print("path sum equal: ", path_sum_III_2(p1, 8))
print("path sum equal: ", path_sum_III_2(p2, 22))
print("path sum equal: ", path_sum_III_2(p3, 3))
print("\n")
obj = Solution()
print("path sum equal: ", obj.path_sum_III_3(p1, 8))
print("path sum equal: ", obj.path_sum_III_3(p2, 22))
print("path sum equal: ", obj.path_sum_III_3(p3, 3))

obj = Solutionk()
print("path sum equal: ", obj.path_sum_III_4(p1, 8))
print("path sum equal: ", obj.path_sum_III_4(p2, 22))
print("path sum equal: ", obj.path_sum_III_4(p3, 3))

obj = Solutionm()
print("path sum equal: ", obj.path_sum_III_5(p1, 8))
print("path sum equal: ", obj.path_sum_III_5(p2, 22))
print("path sum equal: ", obj.path_sum_III_5(p3, 3))


obj = Solutionn()
print("path sum equal: ", obj.path_sum_III_6(p1, 8))
print("path sum equal: ", obj.path_sum_III_6(p2, 22))
print("path sum equal: ", obj.path_sum_III_6(p3, 3))

obj = Solutiono()
print("path sum equal: ", obj.path_sum_III_7(p1, 8))
print("path sum equal: ", obj.path_sum_III_7(p2, 22))
print("path sum equal: ", obj.path_sum_III_7(p3, 3))