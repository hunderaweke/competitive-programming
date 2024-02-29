# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = 0
        hash_map = defaultdict(int)
        hash_map[0] = 1
        def find_sum(node,current_sum=0):
            nonlocal counter
            if not node:
                return 
            current_sum += node.val
            if current_sum - targetSum in hash_map:
                counter += hash_map[current_sum - targetSum]
            hash_map[current_sum] += 1
            find_sum(node.right,current_sum)
            find_sum(node.left,current_sum)
            hash_map[current_sum] -= 1
            return 
        
        find_sum(root)
        return counter