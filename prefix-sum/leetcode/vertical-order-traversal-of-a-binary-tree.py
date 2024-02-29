# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        hash_map = defaultdict(list)
        def inorder(node,row=0,col=0):
            if not node:
                return
            hash_map[(col,row)].append(node.val)
            inorder(node.left,row+1,col-1)
            inorder(node.right,row+1,col+1)
            return
        inorder(root)
        for k in hash_map:
            hash_map[k].sort()
        matrix = list(hash_map.items())
        matrix.sort(key=lambda x: (x[0][1],x[0][0]))
        col_hashmap = defaultdict(list)
        print(matrix)
        for [(col,row),val] in matrix:
            col_hashmap[col].extend(val)
        ans = list(col_hashmap.items())
        ans.sort()
        return [nums for _,nums in ans]