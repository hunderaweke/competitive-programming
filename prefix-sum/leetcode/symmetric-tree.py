# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(node1,node2):
            if node2 and not node1:
                return False
            if node1 and not node2:
                return False
            if not node2 and not node1:
                return True
            if (not node2.right and not node2.left) and (not node1.right and not node1.left):
                return node2.val == node1.val
            return node1.val == node2.val and (same(node1.right,node2.left) and same(node1.left,node2.right))
        return same(root.right,root.left)