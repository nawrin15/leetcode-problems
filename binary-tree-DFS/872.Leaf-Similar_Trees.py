class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p1 = TreeNode(
    val = 3,
    left = TreeNode(
                val = 5, 
                left = TreeNode(
                    val=6, 
                    left=None,
                    right=None
                ),
                right = TreeNode(
                    val=2, 
                    left=TreeNode(
                        val=7, 
                        left=None,
                        right=None
                    ),
                    right=TreeNode(
                        val=4, 
                        left=None,
                        right=None
                    )
                )
        ),
    right = TreeNode(
                val=1, 
                left= TreeNode(
                    val=9, 
                    left=None,
                    right=None
                ), 
                right=TreeNode(
                    val=8, 
                    left=None,
                    right=None
                )
            )
    
)

p2 = TreeNode(
    val = 3,
    left = TreeNode(
                val = 5, 
                left = TreeNode(
                    val=6, 
                    left=None,
                    right=None
                ),
                right = TreeNode(
                    val=7, 
                    left=None,
                    right=None
                )
        ),
    right = TreeNode(
                val=1, 
                left= TreeNode(
                    val=4, 
                    left=None,
                    right=None
                ), 
                right=TreeNode(
                    val=2, 
                    left=TreeNode(
                        val=9, 
                        left=None,
                        right=None
                    ),
                    right=TreeNode(
                        val=8, 
                        left=None,
                        right=None
                    )
                )
            )
    
)

p3 = TreeNode(
    val = 1,
    left = TreeNode(
            val = 2, 
            left = None,
            right = None
        ),
    right = TreeNode(
        val=3, 
        left = None,
        right=None
    )
)
p4 = TreeNode(
    val = 1,
    left = TreeNode(
            val = 3, 
            left = None,
            right = None
        ),
    right = TreeNode(
        val=2, 
        left = None,
        right=None
    )
)

def leafSimilar(root1, root2) -> bool:
    def dfs(root):
        if not root: return []
        if not (root.left or root.right): return [root.val]
        return dfs(root.left) + dfs(root.right)
    print("leaf-1:", dfs(root1))
    print("leaf-1:", dfs(root2))
    return dfs(root1) == dfs(root2)
    
print("is leaf similar: ", leafSimilar(p1, p2))
print("is leaf similar: ", leafSimilar(p3, p4))

