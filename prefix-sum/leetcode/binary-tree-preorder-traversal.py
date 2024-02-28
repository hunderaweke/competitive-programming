# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        traversals= [root.val]
        if root and not root.right and not root.left:
            return traversals
        if root and root.left:
            traversals.extend(self.preorderTraversal(root.left))
        if root and root.right:
            traversals.extend(self.preorderTraversal(root.right))
        return traversals