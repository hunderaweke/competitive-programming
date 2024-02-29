# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # let us have three pointers that will point to the current node
        # the previous node and the start point of the linked list
        # if the current node value is greater than the previous element value we should just continue
        # otherwise start the pointer that is pointing to the head of the linked list and try to find a value which is greater than the current value
        # if we find the node that have a value that is greater insert the node in the middle there
        dummy = ListNode(-inf,head)
        prev = dummy
        current = head
        while current:
            if current and current.val < prev.val:
                start = dummy
                while start.next and start.next.val <= current.val:
                    start = start.next
                removed_node = current
                prev.next = current.next
                current = prev.next
                removed_node.next = start.next
                start.next = removed_node
            else:
                current = current.next
                prev = prev.next
        return dummy.next