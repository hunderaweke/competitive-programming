class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1]*len(nums)
        for i,num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                idx = stack.pop()
                ans[idx] = num
            stack.append(i)
        for i,num in enumerate(nums):
            while stack and nums[stack[-1]] <num:
                idx = stack.pop()
                ans[idx] = num
        return ans