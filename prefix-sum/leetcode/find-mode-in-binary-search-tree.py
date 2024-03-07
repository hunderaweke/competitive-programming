# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        def dfs(node):
            if not node:
                return

            counter[node.val] += 1
            dfs(node.right)
            dfs(node.left)
        dfs(root)
        max_fre = max(counter.values())
        return[n for n in counter.keys() if counter[n] == max_fre]