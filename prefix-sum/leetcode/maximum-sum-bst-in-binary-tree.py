# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def is_valid(val,left_max,right_min):

            if left_max == None:
                left_max = -inf

            if right_min == None:
                right_min = inf

            return left_max < val < right_min
        
        def dfs(node):
            
            if not node:
                return [True,0,None,None]

            valid_left,left_sum,left_min,left_max = dfs(node.left)

            valid_right,right_sum,right_min,right_max = dfs(node.right)

            if valid_left and valid_right and is_valid(node.val,left_max,right_min):
                curr_sum = right_sum + left_sum + node.val
                self.max = max(self.max,curr_sum)

                if right_max == None:
                    right_max = node.val
                    
                if left_min == None:
                    left_min = node.val
                
                return [True,curr_sum,left_min,right_max]
            else:
                return [False,None,None,None]
            
        dfs(root)
        return self.max