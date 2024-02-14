# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101,head)
        current = head
        prev = dummy
        while current:
            while current and current.val == prev.val:
                current = current.next
                prev.next = current
            prev = prev.next
            if current:
                current = current.next
        return head