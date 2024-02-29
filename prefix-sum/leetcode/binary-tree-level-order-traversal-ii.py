# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()

        if root:
            queue.append(root)
    
        while len(queue) > 0:
            level_array = []
            for i in range(len(queue)):
                curr = queue.popleft()
                level_array.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(level_array) 
        return ans[::-1]