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

## problem traverse all path can be logn complexity
##Solution-1
def path_sum_I_1(root, targetSum) -> bool:
    
    def dfs(root, sum):
        if not root: return False
        
        sum += root.val
        if not root.left and not root.right:
            return sum == targetSum
        
        return dfs(root.left, sum) or dfs(root.right, sum)
    
    
    return dfs(root, 0)

##Solution-2 (with using extra variable to store sum)
def path_sum_I_2(root, targetSum) -> bool:
    
    def dfs(root, targetSum):
        if not root: return False
        
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        
        return dfs(root.left, targetSum) or dfs(root.right, targetSum)
    
    
    return dfs(root, targetSum)

print("is path sum equal: ", path_sum_I_1(p1, 22))
print("is path sum equal: ", path_sum_I_1(p2, 5))
print("is path sum equal: ", path_sum_I_1(p3, 0))
print("\n")
print("is path sum equal: ", path_sum_I_2(p1, 22))
print("is path sum equal: ", path_sum_I_2(p2, 5))
print("is path sum equal: ", path_sum_I_2(p3, 0))