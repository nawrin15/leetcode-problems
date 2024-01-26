class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

p1 = TreeNode(
    val=3, 
    left=TreeNode(
        val=5, 
        left=TreeNode(
            val=6, 
            left=None, 
            right=None
        ),
        right=TreeNode(
            val=2, 
            left=TreeNode(
                val=3, 
                left=None, 
                right=None
            ), 
            right=TreeNode(
                val=3, 
                left=None, 
                right=None
            )
        )
    ), 
    right=TreeNode(
        val=1, 
        left=TreeNode(
            val=0, 
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
    val=1, 
    left=TreeNode(
        val=2, 
        left=None, 
        right=None
    ), 
    right=None
)
p3 = TreeNode(
    val=6, 
    left=TreeNode(
        val=2, 
        left=TreeNode(
            val=0, 
            left=None, 
            right=None
        ),
        right=TreeNode(
            val=4, 
            left=TreeNode(
                val=3, 
                left=None, 
                right=None
            ), 
            right=TreeNode(
                val=5, 
                left=None, 
                right=None
            )
        )
    ), 
    right=TreeNode(
        val=8, 
        left=TreeNode(
            val=7, 
            left=None, 
            right=None
        ),
        right=TreeNode(
            val=9, 
            left=None, 
            right=None
        )
    )
)
def lowestCommonAncestor(root, p, q):
    def dfs(root):
        if not root or root.val == p or root.val == q:
            return root
        
        left = dfs(root.left)
        right = dfs(root.right)
        
        if left and right:
            return root
        else:
            return left or right
    
    return dfs(root)        
        


print(lowestCommonAncestor(p1, 5, 1))  #3
print(lowestCommonAncestor(p1, 5, 4))  #5
print(lowestCommonAncestor(p2, 1, 2))  #1
print(lowestCommonAncestor(p3, 2, 8))  #6 