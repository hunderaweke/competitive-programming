# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        left = right = dummy
        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        if left.next:
            left.next = left.next.next
        else:
            left.next = None
        return dummy.next