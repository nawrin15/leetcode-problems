class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


p1 = TreeNode(
    val = 3,
    left = TreeNode(
                val = 1, 
                left = TreeNode(
                    val=3, 
                    left=None,
                    right=None
                ),
                right = None
        ),
    right = TreeNode(
                val=4, 
                left= TreeNode(
                    val=1, 
                    left=None,
                    right=None
                ), 
                right=TreeNode(
                    val=5, 
                    left=None,
                    right=None
                )
            )
    
)

p2 = TreeNode(
    val = 3,
    left = TreeNode(
                val = 3, 
                left = TreeNode(
                    val=4, 
                    left=None,
                    right=None
                ),
                right = TreeNode(
                    val=2, 
                    left=None,
                    right=None
                )
        ),
    right = None
    
)

p3 = TreeNode(
    val = 1,
    left = None,
    right = None
)

def good_nodes_counter(root) -> bool:
    
    def dfs(root, maxValue):
        if not root: return 0
        
        res = 1 if root.val >= maxValue else 0
        maxValue = max(root.val, maxValue)
        
        res += dfs(root.left, maxValue)
        res += dfs(root.right, maxValue)
    
        return res
    
    return dfs(root, root.val)
    
print("good node count: ", good_nodes_counter(p1))
print("good node count: ", good_nodes_counter(p2))
print("good node count: ", good_nodes_counter(p3))

