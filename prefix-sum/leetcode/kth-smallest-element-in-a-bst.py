# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraverse(node):
            traverse = []
            if not node:
                return []
            traverse.extend(inorderTraverse(node.left))
            traverse.append(node.val)
            traverse.extend(inorderTraverse(node.right))
            return traverse
        inorderTraversal = inorderTraverse(root)
        return inorderTraversal[k-1]