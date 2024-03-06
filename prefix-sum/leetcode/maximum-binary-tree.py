# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(arr):
            if not arr:
                return None
            
            max_indx = arr.index(max(arr))
            node = TreeNode(arr[max_indx])
            node.right = dfs(arr[max_indx+1:])
            node.left = dfs(arr[:max_indx])
            return node

        node = dfs(nums)
        return node 