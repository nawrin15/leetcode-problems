# Definition for a binary tree node.
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
#True
p2 = TreeNode(
    val = 1,
    left = TreeNode(
        val = 2, 
        left = TreeNode(
            val = 3,
            left=TreeNode(
                val=4,
                left=None,
                right=None
            ),
            right=TreeNode(
                val=4,
                left=None,
                right=None
            )
        ),
        right = TreeNode(
            val = 3,
            left=None,
            right=None
        )
    ),
    right= TreeNode(
        val = 2,
        left=None,
        right=None
    )
)
#False

p3 = None
#True
def isBalanced(root) -> bool:
    def dfs(root):
        if not root: return True, 0
        isBalancedLeft, left_length = dfs(root.left)
        isBalancedRight, right_length = dfs(root.right)
        is_balance = isBalancedLeft and isBalancedRight and \
            (abs(left_length-right_length) <= 1)
    
        return is_balance, 1 + max(left_length, right_length)
    isBalanced, length = dfs(root)
    return isBalanced
    
print(isBalanced(p1))
print(isBalanced(p2))
print(isBalanced(p3))
