# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,num,target):
            if not node:
                return False
            num += node.val
            if not node.right and not node.left:
                return num == target
            return dfs(node.right,num,target) or dfs(node.left,num,target)
        return dfs(root,0,targetSum)