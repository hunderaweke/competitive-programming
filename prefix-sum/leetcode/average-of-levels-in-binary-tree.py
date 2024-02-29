# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque()
        level = 0
        counter = defaultdict(int)
        if root:
            queue.append((root,level))
        while len(queue) > 0:
            running_sum = 0
            for i in range(len(queue)):
                curr,l = queue.popleft()
                counter[l] += 1
                running_sum += curr.val
                if curr.left:
                    queue.append((curr.left,l+1))
                if curr.right:
                    queue.append((curr.right,l+1))
            if counter[level]:
                ans.append(running_sum/counter[level])
            level += 1
        return ans
