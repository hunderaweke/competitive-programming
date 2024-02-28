# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversals = []
        if root:
            if not root.right and not root.left:
                return [root.val]
            if root.left:
                traversals.extend(self.inorderTraversal(root.left))
            traversals.append(root.val)        
            if root.right:
                traversals.extend(self.inorderTraversal(root.right))
        return traversals