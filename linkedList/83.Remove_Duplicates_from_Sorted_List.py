class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        point = head

        while point and point.next:
            if point.val == point.next.val:
                point.next = point.next.next
            else:
                point = point.next

        return head

# Input: head = [1,1,2]
# Output: [1,2]
head1 = ListNode(
    val = 1,
    next = ListNode(
        val = 1,
        next = ListNode (
            val = 2,
            next = None
        )
    )
)


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
head2 = ListNode(
    val = 1,
    next = ListNode(
        val = 1,
        next = ListNode(
            val = 2,
            next = ListNode(
                val = 3,
                next = ListNode(
                    val = 3,
                    next = None
                )
            )
        )
    )
)


obj = Solution()
print(obj.deleteDuplicates(head1))
print(obj.deleteDuplicates(head2))


