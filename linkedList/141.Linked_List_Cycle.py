# Definition for singly-linked list.
# Solve using  Floyd's Tortoise and Hare / Floyd's Cycle Finding Algorithm
class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False

# head = [3,2,0,-4] pos = 1
e1 = ListNode(
    val = 3,
    next = ListNode(
        val = 2,
        next = ListNode (
            val = 0,
            next = ListNode(
                val = -4,
                next = None
            )
        )
    )
)

e1.next.next.next.next = e1.next

# head = [1,2] pos = 0
e2 = ListNode(
    val = 1,
    next = ListNode(
        val = 2,
        next = None
    )
)
e2.next.next = e2


# head = [1] pos = -1
e3 = ListNode(
    val = 1,
    next = None
)
obj = Solution()
print(obj.hasCycle(e1))
print(obj.hasCycle(e2))
print(obj.hasCycle(e3))


