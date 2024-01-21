class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p1 = TreeNode(
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

p2 = TreeNode(
    val = 1,
    left = TreeNode(
            val = 2, 
            left = None,
            right = None
        ),
    right = TreeNode(
            val = 3, 
            left = None,
            right = None
        ),
    
)

p3 = TreeNode(
    val = 1,
    left = TreeNode(
            val = 2, 
            left = None,
            right = None
        ),
    right = None
)

def path_sum_II_1(root, targetSum) -> bool:
    
    result = []
    
    def dfs(root, sum, path):
        if not root: return None
        
        path.append(root.val)
        sum += root.val
        if not root.left and not root.right and sum == targetSum:
            result.append(path.copy())
        else:
            dfs(root.left, sum, path)
            dfs(root.right, sum, path)
        path.pop()
    
    
    dfs(root, 0, [])
    return result

##Solution-2 (with using extra variable to store sum)
def path_sum_II_2(root, targetSum) -> bool:
    
    result = []
    
    def dfs(root, targetSum, path):
        if not root: return None
        
        path.append(root.val)
        targetSum -= root.val
        if not root.left and not root.right and targetSum == 0:
            result.append(path.copy())
        else:
            dfs(root.left, targetSum, path)
            dfs(root.right, targetSum, path)
        path.pop()    
    
    dfs(root, targetSum, [])
    return result

print("path sum equal: ", path_sum_II_1(p1, 22))
print("path sum equal: ", path_sum_II_1(p2, 5))
print("path sum equal: ", path_sum_II_1(p3, 0))
print("\n")
print("path sum equal: ", path_sum_II_2(p1, 22))
print("path sum equal: ", path_sum_II_2(p2, 5))
print("path sum equal: ", path_sum_II_2(p3, 0))