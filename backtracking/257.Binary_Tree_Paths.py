# Example 1:
# Input: 
root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]
# Example 2:

# Input: 
root = [1]
# Output: ["1"]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
root1 = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=4,
                next=None
            )
        )
    )
root2 = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=4,
                next=None
            )
        ) 
    )    
def binaryTreePaths(root: Optional[TreeNode]):