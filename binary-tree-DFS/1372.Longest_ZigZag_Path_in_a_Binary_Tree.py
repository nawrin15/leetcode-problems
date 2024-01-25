class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
p1 = TreeNode(
    val = 1,
    left = None,
    right = TreeNode(
        val=1, 
        left = TreeNode(
            val=1, 
            left = None,
            right=None
        ),
        right=TreeNode(
            val=1, 
            left = TreeNode(
                val=1, 
                left = None,
                right=TreeNode(
                    val=1, 
                    left = None,
                    right=TreeNode(
                        val=1, 
                        left = None,
                        right=None
                    )
                )
            ),
            right=TreeNode(
                val=1, 
                left = None,
                right=None
            )
        )
    )
)

p2=TreeNode(
    val=1, 
    left = TreeNode(
        val=1, 
        left = None,
        right=TreeNode(
            val=1, 
            left = TreeNode(
                val=1, 
                left = None,
                right=TreeNode(
                    val=1, 
                    left = None,
                    right=None
                )
            ),
            right=TreeNode(
                val=1, 
                left = None,
                right=None
            )
        )
    ),
    right=TreeNode(
        val=1, 
        left = None,
        right=None
    )
)
p3=TreeNode(
    val=1, 
    left = None,
    right=None
)

class Solution:
    def longest_zigzag_path(self, root):
        self.max_val = 0
        
        def dfs(root, dir, depth):
            if not root: return 
            
            self.max_val = max(self.max_val, depth)
            
            if dir == 0:
                dfs(root.left, dir, 1)
                dfs(root.right, dir^1, depth + 1)
            else:
                dfs(root.left, dir^1, depth + 1)
                dfs(root.right, dir, 1)
            return self.max_val

        dfs(root.left, 0, 1)
        dfs(root.right, 1, 1)
        return self.max_val


obj = Solution()
print(obj.longest_zigzag_path(p1))
print(obj.longest_zigzag_path(p2))
print(obj.longest_zigzag_path(p3))
            
    
