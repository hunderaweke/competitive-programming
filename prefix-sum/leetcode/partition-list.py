# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # make two heads one for greater or equal one for less
        # start from the head of the linked list and if the value of the node is greater add to the 
        # greater linked list if it is less add to the less linked list
        # finally set the next of the less linked list to the starting point of the greater
        greater_head = ListNode(-1,None)
        less_head = ListNode(-1,None)
        less = less_head
        greater = greater_head
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        greater.next = None
        less.next = greater_head.next
        return less_head.next 