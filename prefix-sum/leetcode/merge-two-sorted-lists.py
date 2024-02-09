# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Creating two pointers on the first and the second list
        # Checking the minimum value from the two
        # Creating another head
        # Adding the first minimum to the new head
        # moving the pointer with that value to the next position
        # Repeating till one of the pointers rich the end node
        # Iterating on the pointer which haven't get to the last node to the last node and adding the node that the pointer is currently on 
        # Return the new head
        dummy = ListNode()
        ptr1 = list1
        ptr2 = list2
        node = dummy
        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                node.next = ptr1
                node = node.next
                ptr1 = ptr1.next
            else:
                node.next = ptr2
                node = node.next
                ptr2 = ptr2.next
        while ptr1:
            node.next = ptr1
            node = node.next
            ptr1 = ptr1.next
        while ptr2:
            node.next = ptr2
            node = node.next
            ptr2 = ptr2.next
        return dummy.next