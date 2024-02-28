# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # by dividing the problems to a smaller problems 
        # we should go till the end by comparing the maximum of the right ans the left 
        def find_depth(node):
            depth = 1
            if not node:
                return 0
            depth += max(find_depth(node.right),find_depth(node.left))
            return depth
        depth = find_depth(root)
        return depth
        