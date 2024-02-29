# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(cur,num):
            if not cur:
                return 0
            num= num * 10 + cur.val
            if not cur.right and not cur.left:
                return num
            return dfs(cur.right,num) +dfs(cur.left,num)
        return dfs(root,0)
        