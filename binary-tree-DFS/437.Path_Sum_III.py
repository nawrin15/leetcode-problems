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

print("path sum equal: ", path_sum_III_1(p1, 8))
print("path sum equal: ", path_sum_III_1(p2, 22))
print("path sum equal: ", path_sum_III_1(p3, 3))
print("\n")
print("path sum equal: ", path_sum_III_2(p1, 8))
print("path sum equal: ", path_sum_III_2(p2, 22))
print("path sum equal: ", path_sum_III_2(p3, 3))
