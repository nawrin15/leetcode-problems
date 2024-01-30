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
def minDepth2(root) -> int:
    def bfs(root):
        queue =[root]
        level = 0
        while queue:
            level += 1
            print([node.val for node in queue])
            for i in range(len(queue)):
                node = queue.pop(0)
                
                if not (node.left or node.right): 
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
    
    return 0 if not root else bfs(root) 


print(minDepth(p1))
print(minDepth(p2))

print(minDepth2(p1))
print(minDepth2(p2))


          
