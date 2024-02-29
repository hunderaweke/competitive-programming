# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def preorder(node):
            traversal = []
            if not node:
                return traversal
            traversal.append(node)
            if node.left:
                traversal.extend(preorder(node.left))
            if node.right:
                traversal.extend(preorder(node.right))
            return traversal
        traversal = preorder(root)
        if not traversal:
            return
        for i in range(len(traversal)-1):
            traversal[i].right = traversal[i+1]
            traversal[i].left = None
        traversal[-1].left = None
        traversal[-1].right = None
        return root