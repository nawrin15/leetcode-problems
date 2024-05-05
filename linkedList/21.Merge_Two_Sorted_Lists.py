lista1 = [1,2,4]
lista2 = [1,3,4]
#Output: [1,1,2,3,4,4]

listb1 = []
listb2 = []
#Output: []

listc1 = []
listc2 = [0]
#Output: [0]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
lista2 = ListNode(
        val=1,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4,
                next=None
            )
        )
    )
lista1 = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=4,
                next=None
            )
        ) 
    )    

listb1 = None
listb2 = None

listc1 = None
listc2 = ListNode(
        val=0,
        next=None
    )

def mergeTwoLists(list1, list2):
    mergeList = []
    for i in range(max(len(list1), len(list2))):
        a = list1[i] if i < len(list1) else None
        b = list2[i] if i < len(list2) else None
        if a != None:
            mergeList.append(a)
        if b != None:
            mergeList.append(b)
    return mergeList

print(mergeTwoLists(lista1, lista2))
print(mergeTwoLists(listb1, listb2))
print(mergeTwoLists(listc1, listc2))
    
    