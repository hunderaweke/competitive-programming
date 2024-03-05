# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        start = end = head
        parts = length // k
        remaining = length % k
        result = []
        curr = head
        for i in range(k):
            if not curr:
                break
            node = curr
            prev = None
            for _ in range(parts):
                prev = curr
                curr = curr.next
            if remaining:
                prev = curr
                curr = curr.next
                remaining -= 1
            if prev:
                prev.next = None
            result.append(node)
        while len(result) < k:
            result.append(None)
        return result