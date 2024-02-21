# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1 = headA
        ptr2 = headB
        while ptr1 and ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        if not ptr1:
            ptr1 = headB
            while ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            ptr2 = headA
        else:
            ptr2 = headA
            while ptr1:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            ptr1 = headB
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1