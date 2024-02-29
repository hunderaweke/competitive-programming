# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()
        if root:
            queue.append(root)
        left_to_right = True
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                curr= queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if left_to_right:
                ans.append(level)
            else:
                ans.append(level[::-1])
            left_to_right = not left_to_right
        return ans