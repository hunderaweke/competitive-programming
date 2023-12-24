class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indices = {}
        for i,n in enumerate(nums):
            indices[n] = i
        for operation in operations:
            nums[indices[operation[0]]] = operation[1]
            indices[operation[1]] = indices[operation[0]]
            indices.pop(operation[0])
        return nums