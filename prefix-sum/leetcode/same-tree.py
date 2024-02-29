# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if q and not p:
            return False
        if p and not q:
            return False
        if not q and not p:
            return True
        if (not q.right and not q.left) and (not p.right and not p.left):
            return q.val == p.val
        return p.val == q.val and (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))