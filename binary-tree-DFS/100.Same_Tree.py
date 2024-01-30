class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
p1 = TreeNode(
    val = 1,
    left = TreeNode(
                val = 2, 
                left = None,
                right = None
        ),
    right = TreeNode(val=3, left= None, right=None)
)
q1 = TreeNode(
    val = 1,
    left = TreeNode(
                val = 2, 
                left = None,
                right = None
        ),
    right = TreeNode(val=3, left= None, right=None)
)
p2 = TreeNode(
    val = 1,
    left = TreeNode(val=2, left= None, right=None),
    right = None
)
q2 = TreeNode(
    val = 1,
    left = None,
    right = TreeNode(val=2, left= None, right=None)
)

p3 = TreeNode(
    val = 1,
    left = TreeNode(val=2, left= None, right=None),
    right = TreeNode(val=1, left= None, right=None)
)
q3 = TreeNode(
    val = 1,
    left = TreeNode(val=1, left= None, right=None),
    right = TreeNode(val=2, left= None, right=None)
)

def isSameTree(p, q):
    def dfs(root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
    
    return dfs(p,q)

print(isSameTree(p1,q1))
print(isSameTree(p2,q2))
print(isSameTree(p3,q3))
    