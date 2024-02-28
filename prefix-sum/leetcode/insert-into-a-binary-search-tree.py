# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node,val):
            newNode = TreeNode(val,None,None)
            if not node:
                return newNode
            if not node.right and val > node.val:
                node.right = newNode
                return node
            if not node.left and val < node.val:
                node.left = newNode
                return node
            if node.right and val > node.val:
                insert(node.right,val)

            if node.left and val < node.val:
                insert(node.left,val)
            return node 
        return insert(root,val)