# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0

        def dfs(node,high,low):
            nonlocal range_sum
            if not node:
                return
            if node.val >= low and node.val <= high:
                range_sum += node.val
            if node.val >= high:
                dfs(node.left,high,low)
            elif node.val <= low:
                dfs(node.right,high,low)
            else:
                dfs(node.right,high,low)
                dfs(node.left,high,low)
            return

        dfs(root,high,low)

        return range_sum