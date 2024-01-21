class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def maxDepth(root) -> int:
    def dfs(root, depth):
        if not root: return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
    
    return dfs(root, 0)
    

p1 = TreeNode(
    val = 0,
    left = TreeNode(
                val = 0, 
                left = TreeNode(
                    val=0, 
                    left=None,
                    right=None
                ),
                right = TreeNode(
                    val=0, 
                    left=None,
                    right=None
                )
        ),
    right = TreeNode(val=0, left= None, right=None)
)

p2 = TreeNode(
    val = 0,
    left = TreeNode(
                val = 0, 
                left = None,
                right = None
        ),
    right = TreeNode(val=0, left= None, right=None)
)
p3 = TreeNode(
    val = 0,
    left = TreeNode(
                val = 0, 
                left = TreeNode(
                    val=0, 
                    left=None,
                    right=None
                ),
                right = TreeNode(
                    val=0, 
                    left=None,
                    right=None
                )
        ),
    right = TreeNode(
        val=0, 
        left = TreeNode(
                    val=0, 
                    left= TreeNode(
                        val=0, 
                        left=None,
                        right=TreeNode(
                            val=0, 
                            left=None,
                            right=None
                        )
                    ),
                    right=None
        ),
        right=None
    )
)

print(maxDepth(p3))