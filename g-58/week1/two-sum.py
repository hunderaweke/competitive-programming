class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)
        for i in range(n):
            numMap[nums[i]] = i
        for i in range(n):
            comp = target - nums[i]
            if comp in numMap and numMap[comp] != i:
                return [i, numMap[comp]]

