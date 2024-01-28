class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p1 = TreeNode(
    val = 3,
    left = TreeNode(
        val = 9, 
        left = None,
        right = None
    ),
    right = TreeNode(
        val=20, 
        left= TreeNode(
            val=15, 
            left=None,
            right=None
        ), 
        right=TreeNode(
            val=7, 
            left=None,
            right=None
        )
    )
    
)

p2 = TreeNode(
    val = 2,
    left = None,
    right = TreeNode(
        val = 3, 
        left = None,
        right = TreeNode(
            val = 4, 
            left = None,
            right = TreeNode(
                val = 5, 
                left = None,
                right = TreeNode(
                    val = 6, 
                    left = None,
                    right = None
                )
            )
        )
    )
)

##using dfs
def minDepth(root) -> int:
    def dfs(root):
        if not root: 
            return 0
        if not (root.left or root.right): 
            return 1
        if not root.left:
            return 1 + dfs(root.right)
        if not root.right:
            return 1 + dfs(root.left)
        return 1 + min(dfs(root.left),  dfs(root.right))
        
    return dfs(root)

##using bfs
def minDepth(root) -> int:
    def bfs(root):
        if not root: 
            return 0
        if not (root.left or root.right): 
            return 1
        if not root.left:
            return 1 + dfs(root.right)
        if not root.right:
            return 1 + dfs(root.left)
        return 1 + min(dfs(root.left),  dfs(root.right))
        
    return dfs(root)

print(minDepth(p1))
print(minDepth(p2))
          
