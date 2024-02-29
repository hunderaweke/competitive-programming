# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []
        def check_path(node,target,current_path=[],current_sum=0):
            if not node:
                return 
            current_sum += node.val
            current_path.append(node.val)
            if not node.right and not node.left:
                if current_sum == target:
                    paths.append(current_path)
                return
            if node.left:
                check_path(node.left,target,current_path.copy(),current_sum)
            if node.right:
                check_path(node.right,target,current_path.copy(),current_sum)
            return
        check_path(root,targetSum)
        return paths