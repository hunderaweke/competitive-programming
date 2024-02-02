# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First find the cycle using fast and slow pointer
        # Use the warshal way for finding the starting point of the cycle
        # initialize two pointers one from where the slow and fast pointer intersect and another from the head of the linked list
        # increment the first by one and the second decrement by one till they intersect
        # the point of intersection is the solution
        slow,fast = head,head
        there_is_cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                there_is_cycle = True
                break
        if there_is_cycle:
            ptr1 = head
            ptr2 = slow
            while ptr1!=ptr2:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        return ptr1 if there_is_cycle else None